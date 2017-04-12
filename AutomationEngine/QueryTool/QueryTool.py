"""

Created on March 29, 2017

@author Miguel Contreras Morales

History:
4/12/2017 - Adding more queries

"""

from pymongo import MongoClient
import cherrypy as QueryServer
import json


class QueryTool(object):
    """
    QueryTool will contain a subset of functions used to parse
    Mongo Database
    """

    _db = None
    client = None

    def __init__(self, dbaddress="10.30.5.203:27017"):
        """
        Constructor/Intiliazer
        + dbaddress - MongoDB IP
        """

        if (dbaddress == None):
            self._dbaddress = "127.0.0.1:27017"
        else:
            self._dbaddress = dbaddress

        address, port = self._dbaddress.split(':', 2)
        self.client = MongoClient(address, int(port))


    @QueryServer.expose
    def dbdump(self):
        """
        This function will dump out the DBs along with collection stored in DB.
        The function will loop and store names of DB/Collection.
        Secondary check to make sure the DB is up.
        + self - no input required
        """
        print "Initializing DB Dump Query"

        d = dict((db, [collection for collection in self.client[db].collection_names()])
             for db in self.client.database_names())

        return json.dumps(d)


    @QueryServer.expose
    def showdbs(self):
        """
        This function will dump out the DBs in Mongo ONLY
        + self - no input required
        """
        print "Initializing ShowDBs Query"

        dbs = self.client.database_names()

        return json.dumps(dbs)


    @QueryServer.expose
    def showcollections(self, sprocess):
        """
        This function will dump out the collection of DB sprocess
        + sprocess - first level of DB also called 'Collection'
        """
        print "Initializing ShowsCollection Query"

        dbs = self.client.database_names()
        self._db = self.client[sprocess]

        collection = self._db.collection_names(include_system_collections=True)

        return json.dumps(collection)


    @QueryServer.expose
    def showprocess(self, sprocess, pnnum):
        """
        This function will get the number of instances of a specific pnnum in sprocess collection
        + sprocess - the db we will be using
        + pnnum - part number within the db, this is dynamic depending on DB structure
        """
        print "Initializing ShowProcess Query"

        dbquery = ("processid")

        self._db = self.client[sprocess]
        coll = self._db[pnnum]

        return json.dumps(coll.distinct(dbquery))


    @QueryServer.expose
    def processlog(self, sprocess, pnnum, starttime, serialnum):
        """
        This function will get the log for a serialnum at a specfic starttime
        + sprocess - the db we will be using
        + pnnum - part number within the db, this is dynamic depending on DB structure
        + starttime - start time of serialnum
        + serialnum - product indentifier
        """

        print "Initializing Process Log Query"

        dbquery = {'processid.fstarttime': str(starttime),
                   'processid.serialnum': serialnum}

        self._db = self.client[sprocess]
        coll = self._db[pnnum]

        logs = []

        print dbquery

        for dbentry in coll.find(dbquery):
            logs.append(str(dbentry))

        return json.dumps(logs)


    @QueryServer.expose
    def processlogcmd(self, sprocess, pnnum, starttime, serialnum, cmd):
        """
        This function will get the cmds for a serialnum at a specfic starttime
        + sprocess - the db we will be using
        + pnnum - part number within the db, this is dynamic depending on DB structure
        + starttime - start time of serialnum
        + serialnum - product indentifier
        + cmd - command being parsed
        """

        print "Initializing Process Log CMD Query"

        cmd = str(cmd) + "\r"
        cmd = cmd.lower()

        dbquery = {'processid.fstarttime': str(starttime),
                   'processid.serialnum': serialnum,
                   'content.cmdobject.cmd': cmd}

        self._db = self.client[sprocess]
        coll = self._db[pnnum]

        logs = []

        print dbquery

        for dbentry in coll.find(dbquery):
            logs.append(str(dbentry))

        return json.dumps(logs)


    @QueryServer.expose
    def processlogbufferregex(self, sprocess, pnnum, starttime, serialnum, regex):
        """
        This function will get the objext for a serialnum at a specfic starttime that matches
        the regular expression provided
        + sprocess - the db we will be using
        + pnnum - part number within the db, this is dynamic depending on DB structure
        + starttime - start time of serialnum
        + serialnum - product indentifier
        + regex - regular expression
        """

        print "Initializing Process Log Buffer REGEX Query"

        dbquery = {'processid.fstarttime': str(starttime),
                   'processid.serialnum': serialnum,
                   'content.response.buffer': {'$regex': regex}}

        self._db = self.client[sprocess]
        coll = self._db[pnnum]

        logs = []

        print dbquery

        for dbentry in coll.find(dbquery):
            logs.append(str(dbentry))

        return json.dumps(logs)

