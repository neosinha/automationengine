'''
Created on Mar 30, 2017

@author: nsinha
'''

from collections import OrderedDict
import re


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


class ParseExtract(object):
    """
    Handle buffer parsing from pre-defined
    regular expressions
    """
    _regex_dict = {}
    
    def __init__(self):
        pass
    
    def addparser(self, key, regex):
        """
        Add regular expression to be stored
        and called upon during parsing activity.
        
        After defining regex, use extract for matching
        
        + key - name of regex
        - regex - regular expression
        """
        self._regex_dict[key] = re.compile(regex)
        
    def extract(self, buffer, *keys):
        """
        Extract regex from buffer from predefined
        key using re.search()
        
        Returns dictionary in format of {key: matchtext}
        
        If regex included group(s), matchtext will be last
        group matched
        """
        returndict = {}

        for key in keys:
            returndict[key] = None

            if key not in self._regex_dict:
                continue

            regexresult = re.search(self._regex_dict[key], buffer)

            if regexresult:
                # length of groups will indicate last item to group and return
                num_groups = len(regexresult.groups())
                returndict[key] = regexresult.group(num_groups)

        return returndict


# def test_parse_extract():
#     buffer = """
#         hi this is james and this
#         is my test_parse_extract module code.
#         version = 10.125.3:A2
#         we can create regex's and take action
#         based on the key value defined
#         by the user
#     """
#     parse = ParseExtract()
#      
#     parse.addparser('james', 'hi.this.*(ja.es)')
#     parse.addparser('version', 'version.=.(.*)')
#     parse.addparser('module', 'module')
#      
#     print parse.extract(buffer, 'james', 'version', 'module')
#      
# test_parse_extract()


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
