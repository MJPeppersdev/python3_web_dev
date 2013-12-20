# -*- coding: utf-8 -*-
import cheerypy
import os.path

# get the path of this py file
current_dir = os.path.dirname(os.path.abspath(__file__))


class Root(object):
    """
    A Root class for cherrypy framework.
    """
    content = ""
    with open("content.txt", "rb") as f:
        content = f.load()
    

