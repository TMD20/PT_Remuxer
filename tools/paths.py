import tempfile
import re
import os
import pathlib
import subprocess
import functools
import shutil
import itertools
import traceback

import natsort

import config as config
import tools.general as utils
import tools.commands as commands
import tools.logger as logger

tempDirs=[]
def createTempDir():
    tempDir=tempfile.mkdtemp(prefix=config.tempPrefix, dir=config.tempFolder)
    tempDirs.append(tempDir)
    return tempfile.mkdtemp(prefix=config.tempPrefix, dir=config.tempFolder)
def getOldTempPathDirs():
    criticalTime = utils.convertArrow("01","hh")
    results=search(config.tempFolder,f"/{config.tempPrefix}[^/]*$",dir=True)
    return list(filter(lambda x:utils.convertArrow(os.stat(x).st_mtime)>criticalTime,results))
def getTempDirs():
    return tempDirs
def deleteTempDirs():
    folders=getTempDirs()
    for folder in list(filter(lambda x: os.path.exists(x),folders)):
        shutil.rmtree(folder)
    folders=getOldTempPathDirs()
    for folder in list(filter(lambda x: os.path.exists(x),folders)):
        shutil.rmtree(folder)
def search(path,query,case=False,dir=False,ignore=[],fullMatch=False,recursive=True):
    searchMethod=re.search
    if fullMatch==True:
        searchMethod=re.match
    globSearch="**/*"
    if recursive==False:
        globSearch="*/"
    paths = list(map(lambda x: str(x),list(pathlib.Path(path).glob(globSearch))))
    paths=list(natsort.natsorted
    (paths))
    filtered=_excludeHelper(paths,dir,ignore)
    if case:
        return list(filter(lambda x:searchMethod(query,x),filtered))
    else:
        return list(filter(lambda x:searchMethod(query,x,re.IGNORECASE),filtered))
def _excludeHelper(paths,dir,ignore):
    regexPattern=re.compile("|".join(ignore))
    filtered=list(filter(lambda x:os.path.isdir(x)==dir,paths))
    filtered=list(filter(lambda x:len(regexPattern.pattern)==0 or re.search(regexPattern,x)==None,filtered))
    return filtered

def mkdirSafe(target):
    directories = list(reversed(pathlib.Path(target).parents))
    if len(os.path.splitext(target)[1]) == 0:
        directories.append(target)
    for ele in directories:
        if not os.path.exists(ele):
            os.mkdir(ele)
def rmSafe(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


def extractISO(source, inpath):
    basename = f"{os.path.basename(os.path.dirname(source))}_Extracted"
    outPath = os.path.join(inpath, basename)
    if os.path.exists(outPath):
        opts = ["Yes", "No"]
        remove = utils.singleSelectMenu(
            opts, f"Files already extraced\nDo you want to delete the folder:\n {outPath} ",default="No")
        if remove == "No":
            return search(outPath, "STREAM",dir=True)[0]
    return _extractISOProcessor(source,outPath)
            
    
def _extractISOProcessor(source,outPath):
    rmSafe(outPath)
    mkdirSafe(outPath)
    commandlist = [functools.partial(
        _ISOBinaryExtractHelper, source, outPath), functools.partial(_udevilExtractHelper, source, outPath)]
    for command in commandlist:
        try:
            command()
            break
        except Exception as e:
            logger.print(traceback.format_exc(),style="white")
            logger.print(e)
            rmSafe(outPath)
            continue
    if os.listdir(outPath) == 0:
        raise RuntimeError("Issue Extracting Files")

    if utils.singleSelectMenu(["Yes","No"],f"Do you want to remove the ISO?\n{source}",default="No")=="Yes":
        os.remove(source)
    return search(outPath, "STREAM",dir=True)[0]

def _ISOBinaryExtractHelper(source, outPath):
    command = list(itertools.chain.from_iterable([commands.isoBinary(), [
                   "x", convertPathType(source, "Linux"),  "-bsp1","-y" ,f"-o{outPath}", ]]))
    with subprocess.Popen(command) as p:
        p.wait()
        if p.returncode!=0:
            raise Exception("7z Extraction Error")

def _udevilExtractHelper(source, outPath):
    logger.print("\nTrying Mounting ISO\nThen Extracting")
    mountpoint = f"/media/{os.getlogin()}/custom"
    mkdirSafe(f"/media/{os.getlogin()}")
    if os.path.exists(mountpoint):
        subprocess.run(
            ["udevil", "umount", mountpoint], subprocess.PIPE)
    subprocess.run(
        ["udevil", "mount", source, mountpoint], stdout=subprocess.PIPE)

    shutil.copytree(mountpoint, os.path.join(outPath))
    subprocess.run(
        ["udevil", "umount", mountpoint], subprocess.PIPE)

def convertPathType(folder, type):
    if type == "Linux":
        return str(pathlib.PurePosixPath(folder))
    return str(pathlib.PureWindowsPath(pathlib.PurePosixPath(folder)))

def switchPathType(folder):
    if utils.getSystem() == "Linux":
        return convertPathType(folder,"Windows")
    return convertPathType(folder,"Linux")

def listdir(path=None):
    path= path or "."
    if os.path.isdir(path):
        paths=list(pathlib.Path(path).iterdir())
        paths=list(map(lambda x: str(x),paths))
        return list(natsort.natsorted
    (paths))
    return []

def copytree(source,dest):
    shutil.copytree(source,dest,dirs_exist_ok=True)
def move(source,dest):
    shutil.move(source,dest)   
def getParentDir(path,level=0):
    parents=pathlib.Path(path).parents
    if level>=len(parents):
        return
    return str(parents[level])
