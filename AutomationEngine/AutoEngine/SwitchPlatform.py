'''
Created on Mar 30, 2017

@author: nsinha
'''
from AutoEngine.Design import Design
from AutoEngine.AutomationSequence import CommandObject
from AutoEngine.AutomationSequence import ParseEngine
from AutoEngine.AutomationSequence import SequenceStep


class SwitchPlatform(Design):
    '''
    Examlple Product Definition
    '''

    autoSequenceSteps = {}
    commands = []

    def __init__(self, designid="SwitchPlatform1", sprocess=["A1"]):
        '''
        Constructor
        '''
        Design.__init__(self)
        self.setDesignIdName(designid, sprocess)
        self.addProcessName("A2")
        self.setProcessIdentifierName("serialnum")
        self.setProcessIdentifierName("partnum")

        # self.__init_processes()
        # self.loadCommands()
        self.versionCheckSteps()

    def __init_processes(self):
        """
        Initialize Processes
        """
        for pname in self.getProcessNames():
            self.autoSequenceSteps[pname] = []

    def versionCheckPassed(self, response):
        """
        """
        print "Version Check Callback"
        print "===Processing buffer==\n%s" % (response)

    def versionCheckSteps(self):
        """
        """
        seqStep = SequenceStep("CheckVersion")
        seqStep.addSequenceStep("Goto Privilleged prompt",
                                CommandObject(cmdstr='en', timeout=3, prompt='NetIron.*>'))
        seqStep.addSequenceStep("Goto Pageless",
                                CommandObject(cmdstr='skip', timeout=3, prompt='NetIron.*#'))

        pext = ParseEngine(
            'version', 'IronWare.:.Version(.*)Copyright', '5.7.0bT163', matchcallback=self.versionCheckPassed)
        pext.addparser('mbridge', 'MBRIDGE.Revision.:.(.*)', '37')
        pext.addparser(
            'serialnum', 'Module.Active..Serial #:\s(.*),',
            'BVR3810M999')

        # define the show version command
        cmdObj = CommandObject(cmdstr='show version',
                               timeout=3, prompt='NetIron.*#')
        cmdObj.addParseExtract(pext)
        seqStep.addSequenceStep("Show Version", cmdObj)

        self.autoSequenceSteps["versioncheck"] = seqStep

    def loadCommands(self):
        """
        Sample function which loads commands either from a db 
        File or just explictly specifies it..
        """
        self.commands.append(
            CommandObject(cmdstr='en', timeout=3, prompt='NetIron.*>'))
        self.commands.append(
            CommandObject(cmdstr='skip', timeout=30, prompt='NetIron.*#'))
        self.commands.append(
            CommandObject(cmdstr='show chassis', timeout=30, prompt='NetIron.*#'))
        self.commands.append(
            CommandObject(cmdstr='show version', timeout=30, prompt='NetIron.*#'))

    def getAutoSequenceSteps(self):
        """
        """
        return self.autoSequenceSteps

    def getCommands(self):
        """
        Returns the command List
        """
        return self.commands
