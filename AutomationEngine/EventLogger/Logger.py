'''
Created on Mar 29, 2017

@author: nsinha
'''

from pymongo import MongoClient
from datetime import datetime
import time


class Logger(object):
    '''
    Logger class
        1. interacts with a MongoDb instance 
        2. Creates a process unit identifier and   
    '''

    _dbaddress = None
    _db = None
    _col = None
    _sprocess = None
    _starttime = None

    processid = {}

    def __init__(self, sprocess, processIdentifierDict, collectionKey, dbaddress="10.30.5.203:27017"):
        '''
        Constructor
        '''
        if (dbaddress == None):
            self._dbaddress = "127.0.0.1:27017"
        else:
            self._dbaddress = dbaddress

        address, port = self._dbaddress.split(':', 2)
        client = MongoClient(address, int(port))
        self._db = client[sprocess]

        self._starttime = self.getepoch()
        self._col = self._db[processIdentifierDict[collectionKey]]

        # self.processid = {'serialnum': serialnum, 'partnum': partnum,
        #                  'starttime': self._starttime, 'fstarttime': self.getepoch()}
        self.processid = processIdentifierDict
        self.processid['starttime'] = self._starttime
        self.processid['fstarttime'] = self.get_ts(self._starttime, tz=True)

        print "Starting Logging for Epoch: %s , Process: %s with Process Keys %s" % (self._starttime, sprocess, self.processid.keys())

    def loginsert(self, logtype="msg", logobjstr=""):
        """
        Insert log object
        """
        logobj = {'processid': self.processid,
                  'logtype': logtype.trim(),
                  'eventtime': self.getepoch(),
                  'content': logobjstr}

        self._col.insert_one(logobj)

    def logcmd(self, cmdobj):
        """
        Inserts a cmd obj in the log command 
        """
        logobj = {'processid': self.processid,
                  'logtype': "cli",
                  'eventtime': self.getepoch(),
                  'content': cmdobj}

        self._col.insert_one(logobj)

    def get_ts(self, timestamp=None, tz=False):
        """
        Returns a formatted time-stamp for use in logs
        + tz = Returns with timezone information appended
        """
        utime = time.strftime('%Y-%m-%d %H:%M:%S',
                              time.localtime(timestamp / 1000))
        utimez = time.strftime('%Y-%m-%d %H:%M:%S %Z',
                               time.localtime(timestamp / 1000))
        print "Time: --> %s" % (utime)
        print "Time: --> %s" % (utimez)
        ut = utime
        if tz:
            ut = utimez
        print "Time: --> %s" % (ut)
        return ut.replace(':', '-').replace(' ', '-')

    def getepoch(self):
        """
        Returns the epoch 
        """
        millis = int(round(time.time() * 1000))
        return millis
