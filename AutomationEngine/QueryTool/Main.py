"""

Created on April 14, 2017

@author Miguel Contreras Morales

"""


import QueryTool
import datetime
import cherrypy as QueryServer
import os


if __name__ == "__main__":
    """
    This initializes CherryPy services
    + self - no input required
    """

    print "Intializing!"

    portnum = 9100

    # start the QeueryServer
    QueryServer.config.update({'server.socket_host' : '127.0.0.1',
                            'server.socket_port': portnum,
                            'server.socket_timeout': 600,
                            'server.thread_pool' : 8,
                            'server.max_request_body_size': 0
                            })

    wwwPath = os.path.join(os.getcwd(),'www')

    print wwwPath

    staticdir = './www'

    print staticdir

    conf = {
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.on': True,
                'tools.staticdir.dir': wwwPath
            }
        }

    QueryServer.quickstart(QueryTool.QueryTool(dbaddress="10.30.5.203:27017", path= wwwPath), '/', conf)

