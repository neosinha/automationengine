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

    def __init__(self, sequenceName=None):
        '''
        Constructor
        '''
        self.__name = sequenceName

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


class ParseEngine(object):
    """
    Handle buffer parsing from pre-defined
    regular expressions
    """
    _parse_dict = {}
    
    def __init__(self):
        pass
    
    def addparser(self, key, regex=None, known_val=None):
        """
        Add regular expression to be stored
        and called upon during parsing activity.
        
        After defining regex, use extract for matching
        
        + key - name of regex
        + regex - regular expression of item to search for
        + known_val - value to compare against
        """
        self._parse_dict[key] = {
                'regex': regex, 'found_val': None, 'known_val': known_val, 'match': False}

    def extract(self, buffer, *keys):
        """
        Extract regex from buffer from predefined
        key using re.search()
        
        Returns dictionary in format of
            {key: {
                   'mtext': None, - string (matched text)
                   'result': False - boolean (True/False)
                   }
                }
        
        If regex included group(s), matchtext will be last
        group matched
        """
        returndict = {}

        for key in keys:
            if key not in self._parse_dict:
                continue

            returndict[key] = {'mtext': None, 'result': False}

            d = self._parse_dict[key]

            regexresult = re.search(d['regex'], buffer)

            if regexresult:
                # length of groups will indicate last item to group and return
                num_groups = len(regexresult.groups())
                mtext = regexresult.group(num_groups)

                returndict[key]['mtext'] = mtext

                if str(mtext) == str(d['known_val']):
                    returndict[key]['result'] = True

        return returndict


def test_parse_extract():
    buffer = """
        hi this is james and this
        is my test_parse_extract module code.
        version = 10.125.3:A2
        we can create regex's and take action
        based on the key value defined
        by the user
    """
    parse = ParseEngine()

    parse.addparser('james', 'hi.this.*(ja.es)')
    parse.addparser('module', 'module')
    parse.addparser('version', 'version.=.(.*)', '10.125.3:A2')

    result = parse.extract(buffer, 'james', 'version', 'module')

    for key, val in result.iteritems():
        print key, val

if __name__ == "__main__":
    test_parse_extract()


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
