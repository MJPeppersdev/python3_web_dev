# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:55:24 2013

@author: yuankunluo
"""

import cherrypy

class Node(object):
    
    exposed = True
    
    def __call__(self):
        return "The Node content"


class Root(object):
    
    def __init__(self):
        self.node = Node()
    
    @cherrypy.expose
    def index(self):
        return "The index of Root object"
    
    
    @cherrypy.expose
    def page(self):
        return "This is the \"page\" content"
        
    

if __name__ == "__main__":
    cherrypy.quickstart(Root())