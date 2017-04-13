'''
Created on Mar 29, 2017

@author: Navendu Sinha
'''

from TelnetAcessorLib.TelnetAccessor import TelnetAccessor
from EventLogger.Logger import Logger
from AutoEngine.SwitchPlatform import SwitchPlatform
import argparse
import sys
import time


class AutomationApplication(object):
    '''
    classdocs
    '''

    uut = None
    tsession = None
    logger = None

    def __init__(self, console, sprocess, designObj):
        '''
        Constructor
        '''
        self.uut = designObj
        self.uut.__class__ = designObj.__class__
        self.logger = Logger(
            sprocess, self.uut.getProcessIdentifiers(), "partnum")

        self.tsession = TelnetAccessor(debugFlag=True)
        self.tsession.open_console(console)
        """
        """
        # self.tsession.sendexpect()
        # print "%s ==> " % (self.uut.getAutoSeqeunceSteps())
        for stepName in self.uut.getAutoSequenceSteps():
            print "SequenceName: %s" % (stepName)
            stepObj = self.uut.getAutoSequenceSteps()[stepName]
            for step, cmdobj in stepObj.getSequenceSteps().items():
                print "\tCommandObj: %s, %s" % (step, cmdobj.getCommand())
                # print "%s " %
                # (self.uut.getAutoSequenceSteps()[stepName].getCommand())

        # for cmd in self.uut.getCommands():
        #    print "==> %s" % (cmd.getCommand())
            # data = cmd.getCommand()['cmd']
            # matchlist = [cmd.getCommand()['prompt']]
            # timeout = cmd.getCommand()['timeout']
            # resp = self.tsession.sendexpect(data=data,
            #                                matchlist=matchlist,
            #                                timeout=timeout)
            # print buff['timeout_occured']
            # print buff['buffer']
            # cmdobj = {'cmdobject': cmd.getCommand(), 'response': resp}
            # print "==> %s" % (cmdobj)
            # self.logger.logcmd(cmdobj)

if __name__ == "__main__":

    # print "==> %s" % (sys.argv)
    # print "==> %s" % (sys.argv[2])

    designid = sys.argv[2]

    parser = argparse.ArgumentParser(description='Automation Engine')
    parser.add_argument('--designid', help='Design Id which the engine should invoke',
                        required=True)
    parser.add_argument('--console', help='Main Telnet console',
                        required=True)

    parser.add_argument('--sprocess', help='Automation Process to be started',
                        required=True)

    # Instantiate the class correspondig to the given desgin ID
    sw = SwitchPlatform(designid=designid, sprocess=["A1"])

    # Extract and indentify the unique process identifiers for the design
    # A check shall be performed to ensure that the process identifiers are indeed
    # present. This shall be done via argparse

    print "ParserArg: %s" % (parser)
    for key in sw.processIdentifier.keys():
        print "Adding design args:  %s" % (key)
        parser.add_argument("--%s" % (key),
                            help=" is necessary for %s" % (designid), required=True)

    # parse the arguments
    pargs = vars(parser.parse_args())
    for key in sw.getProcessIdentifiers().iterkeys():
        print "Assign processing identifier %s to %s" % (key, pargs[key])
        sw.setProcessIdentifier(key, pargs[key])

    sw.setProcessIdentifier("designid", designid)

    # checking process identifier assignment
    # for key, value in sw.getProcessIdentifiers().items():
    #    print "ProcessId: %s Value: %s" % (key, value)

    ae = AutomationApplication("10.31.248.186:3016", "A1", sw)
    # ae.execProcess(processname="A1")
