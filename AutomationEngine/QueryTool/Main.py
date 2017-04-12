"""

Created on April 14, 2017

@author Miguel Contreras Morales

"""


import QueryTool
import datetime
import cherrypy as QueryServer


class QueryAccessor(object):

    def __init__(self):
        self.q = QueryTool.QueryTool()

    def QueryInitiliaze(self):
        QueryServer.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 9100,})
        QueryServer.quickstart(self.q)


if __name__ == "__main__":

    print "Intializing!"
    QueryAccessor().QueryInitiliaze()


