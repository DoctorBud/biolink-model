"""Generate dotfiles

"""

import logging
import os
import sys

from .schemautils import *
import yaml
import logging
from .manager import *
from .generator import Generator
from graphviz import Digraph


def write_dot(schema, fn, classname=None):
    gen = DotGenerator(schema=schema)

    gen.tr(classname=classname)
    gen.dot.save(fn + '.gv')

def write_all_to_directory(schema, dirname):
    gen = DotGenerator(schema=schema)
    for c in schema.classes:
        cn = gen.manager.class_name(c)
        basepath = "{}/{}".format(dirname, cn)
        write_dot(schema, basepath, c.name)

class DotGenerator(Generator):

    def __init__(self, **args):
        """
        Create a new instance
        """
        super().__init__(**args)
        self.visited = {}


    def tr(self, classname=None):
        schema = self.schema
        mgr = self.manager


        graph_attr={
            'fontsize': '32',
            'penwidth': '5'
        }
        node_attr={
            'shape': 'rectangle',
            'color': 'black',
            'fontname': 'times bold'
        }
        edge_attr={
            'color': 'gray',
            'fontcolor': 'darkgray'
        }

        dot = Digraph(comment=schema.name, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr)
        self.dot = dot


        clist = [c.name for c in schema.classes]
        for c in schema.classes:
            if classname == None or c.name == classname or mgr.class_name(c.name) == classname:
                self.tr_class_uml(c, root=True, recurse=True)

        return dot


    def tr_slot(self, s):
        pass

    def tr_class_uml(self, c, root=False, recurse=False):
        schema = self.schema
        mgr = self.manager
        dot = self.dot

        if c in self.visited:
            return
        self.visited[c] = True

        mgr = self.manager
        cn = c.name
        style = 'bold' if root else 'solid'
        dot.node(cn, ' ' + c.name + ' ', style=style)

        parent = c.is_a
        if parent is not None:
            dot.edge(parent, cn, label='', dir='back', arrowtail='onormal')
            pass

        slots = mgr.class_slotdefs(c, True, True)
        slots.reverse()

        for sn in slots:
            s = mgr.slotdef(sn, c)
            r = mgr.class_slot_range(c, s)
            rc = mgr.classdef(r)
            if rc:
                sym = '-{} >'.format(sn)
                dot.edge(cn, r, label=sn)

                if recurse:
                    self.tr_class_uml(rc, recurse=True)
            else:
                pass

