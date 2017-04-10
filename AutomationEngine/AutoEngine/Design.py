'''
Process definitions are used to define the process flow, and structural requirements 
for each process step for every design unit

This has been written in a dictionary format to allow a simple verbose structure 

Created on Mar 29, 2017
@author: nsinha
'''
from AutoEngine.AutomationSequence import ProcessSequenceStep


class Design(object):
    """
    """
    __designId = None
    __processList = None
    processIdentifier = None
    processAutomationSteps = {}

    def __init__(self):
        """
        + designId : 
        + sprocess : 
        """
        self.__processList = []
        self.processIdentifier = {}

    def setDesignIdName(self, designIdName, sprocess=["A1"]):
        """
        Set design id name
        """
        self.__designId = DesignIdentifier(designIdName)

        # Adds the default process ids

        for sproc in sprocess:
            self.__processList.append(sproc)

    def addProcessName(self, processName):
        """
        Adds a process name to the design
        """
        self.__processList.append(processName)
        self.processAutomationSteps[
            processName] = ProcessSequenceStep(processname=processName)

    def addProcessStepName(self, processName, stepName):
        """
        Adds a process name to the design
        """
        self.processAutomationSteps[
            processName] = ProcessSequenceStep(processname=processName)

    def setProcessIdentifierName(self, idx):
        """
        Sets the process identifier name
        """
        self.processIdentifier[idx] = None

    def setProcessIdentifier(self, idx, value):
        """
        Sets the process identifier name
        """
        self.processIdentifier[idx] = value

    def getProcessIndentifier(self, idx):
        """
        Returns the Process Identifier value corresponding to id
        """
        return self.processIdentifier[idx]

    def getProcessNames(self):
        """
        Returns a list of process names
        """
        return self.__processList

    def getProcessIdentifiers(self):
        """
        Returns the process identifiers for the process
        """
        return self.processIdentifier

    def getProcessSeqeunceSteps(self):
        """
        Returns the dict of Process Sequence Steps
        """
        return self.processAutomationSteps


class DesignIdentifier(object):
    """
    Design Identifiert class
    """

    __name = None
    __major = None
    __minor = None
    __patch = None
    __delimiter = "-"

    def __init__(self, designName, majorRev=None, minorRev=None, patch=None):
        """
            + designName : Design identifier name
        """
        self.name = designName
        self.__major = majorRev
        self.__minor = minorRev
        self.__patch = patch

    def setMajorRev(self, majorRev):
        """
        Sets the major revision
        """
        self.__major = majorRev

    def setMinorRev(self, minorRev):
        """
        Sets the minor revision
        """
        self.__minor = minorRev

    def setPatch(self, patchRev):
        """
        Sets the patch revision
        """
        self.__patch = patchRev

    def getDesignIndetifier(self):
        """
        Constructs and returns the design identifier 
        """
        dId = "%s%s%s%s%s%s%s%s" % (
            self.__name, self.__delimiter,
            self.__major, self.__delimiter,
            self.__minor, self.__delimiter,
            self.__patch, self.__delimiter)

        return dId


class ProcessIdentifiers(object):
    """
    Process Identifier class
    """

    __uniqueid = []

    def __init__(self):
        """
        + uniqueid : This is the unique id of which identifies the unit
        """
        pass

    def addProcessId(self, processId):
        """
        Defines the uniqueProcessId and if it is mandatory
        """
        self.__uniqueid.append(processId)

    def getProcessIdList(self):
        """
        Returns the UniqueId for the design
        """
        return self.__uniqueid
