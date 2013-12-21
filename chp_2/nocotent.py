# -*- coding: utf-8 -*-
import cherrypy
import os.path

# get the path of this py file
current_dir = os.path.dirname(os.path.abspath(__file__))


class Root(object):
    """
    A Root class for cherrypy framework.
    """
    content = ""
    with open("content.txt", "rb") as f:
        content = f.read()
    
    @cherrypy.expose
    def index(self):
        return Root.content
  
if __name__ == "__main__":
    
    root = Root()
    
    cherrypy.quickstart(root, config = {
        '/static':
		{ 'tools.staticdir.on':True,
		  'tools.staticdir.dir':current_dir+"/static"
		}})

