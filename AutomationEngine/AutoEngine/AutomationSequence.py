'''
Created on Mar 30, 2017

@author: nsinha
'''

from collections import OrderedDict


class ProcessSequenceStep(object):
    '''
    classdocs
    '''

    __processname = None
    __sequenceSteps = []

    def __init__(self, processname):
        """
        Initiallizes the Process Sequence Step with a processname 
        """
        self.__processname = processname
        self.__sequenceSteps = {}

    def addProcessSequenceStep(self, step):
        """
        Adds Sequence Step
        """
        self.__sequenceSteps.append(step)

    def getProcessSequenceSteps(self):
        """
        Returns the sequence Steps
        """
        return self.__sequenceSteps


class SequenceStep(object):
    '''
    classdocs
    '''

    __name = None
    __cmdObject = OrderedDict()

    parsedict = None

    def __init__(self, sequenceName=None):
        '''
        Constructor
        '''
        self.__name = sequenceName
        self.parsedict = {}

    def addParseExtract(self, varname, regexp):
        """
        Add a ParseExtract Object
        """
        self.parsedict[varname] = regexp

    def addSequenceStep(self, stepName, cmdObject):
        """
        Adds a command object with a stepName 
        """
        self.__cmdObject[stepName] = cmdObject

    def getSequenceSteps(self):
        """
        Returns the SequenceStep steps ordered dictionary
        """
        return self.__cmdObject


class CommandObject(object):
    """
    Command Object Definition
    """

    cmdstr = None
    timeout = None
    prompt = None
    buffer = None

    def __init__(self, cmdstr, timeout, prompt):
        """
        Command Object 
        """
        self.cmdstr = "%s\r" % (cmdstr)
        self.timeout = timeout
        self.prompt = prompt

    def getCommand(self):
        """
        Get Command
        """
        return {"cmd": self.cmdstr, "timeout": self.timeout, "prompt": self.prompt}
