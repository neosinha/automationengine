'''
Process definitions are used to define the process flow, and structural requirements 
for each process step for every design unit

This has been written in a dictionary format to allow a simple verbose structure 

Created on Mar 29, 2017
@author: nsinha
'''

# define an empty Statistical process container
sprocess = {}

# define list of process steps
sprocess['process'] = {'AProcess1'}


class Design(object):
    """
    """
    __designId = None
    __processList = None

    def __init__(self, designIdName, sprocess=["A1"]):
        """
        + designId : 
        + sprocess : 
        """
        self.__processList = []
        self.__designId = DesignIdentifier(designIdName)
        for sproc in sprocess:
            self.__processList.append(sproc)

    def addProcessName(self, processName):
        """
        Adds a process name to the design
        """
        self.__processList.append(processName)


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

    __uniqueid = None

    def __init__(self, uniqueid):
        """
        + uniqueid : This is the unique id of which identifies the unit
        """
        self.__uniqueid = uniqueid

    def getUniqueId(self):
        """
        Returns the UniqueId for the design
        """
        return self.__uniqueid
