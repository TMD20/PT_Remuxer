import os

import config
import tools.general as utils

def bdSup():
    bdSubBin = config.bdSupSystemPath
    if not os.path.isfile(bdSubBin):
        bdSubBin = config.bdSupProjectPath
    wineBin = config.wineSystemPath
    if not os.path.isfile(wineBin):
        wineBin = config.wineProjectPath
    if utils.getSystem()=="Linux":

        return [wineBin,bdSubBin]
    else:
        return [bdSubBin]
def eac3to():
    eactoBin = config.eac3toSystemPath
    if not os.path.isfile(eactoBin):
        eactoBin = config.eac3toProjectPath

    wineBin = config.wineSystemPath
    if not os.path.isfile(wineBin):
        wineBin = config.wineProjectPath
    if utils.getSystem()=="Linux":
        return [wineBin, eactoBin]
        
    else:
        return [eactoBin]

def bdinfo():
    bdinfoBin = config.bdinfoSystemPath
    if not os.path.isfile(bdinfoBin):
        bdinfoBin = config.bdinfoProjectPath

    wineBin = config.wineSystemPath
    if not os.path.isfile(wineBin):
        wineBin = config.wineProjectPath
    if utils.getSystem()=="Linux":
        return [wineBin, bdinfoBin]
    else:
        return [bdinfoBin]

def mkvmerge():
    if utils.getSystem()=="Linux":
        mkvmergeBin = config.mkvmergeSystemPath
        if not os.path.isfile(mkvmergeBin):
            mkvmergeBin = config.mkvMergeLinux
        return [mkvmergeBin]
    else:
        return [config.mkvMergeWindows]
        

def isoBinary():
    if utils.getSystem() == "Linux":
        return [config.isoExtractLinux]
    else:
        return [config.isoExtractWindows]

def dgdemux():
    if utils.getSystem() == "Linux":
        return [config.dgDemuxLinux]
    else:
        return [config.dgDemuxWindow]