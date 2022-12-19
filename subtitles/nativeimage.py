import os
import traceback

import tools.logger as logger
import tools.directory as dir

import os



try:
    import mediatools.BDSupReader.bdsupreader as BDSup
except ModuleNotFoundError as E:
    BDSup=None
    logger.print(E)
    logger.print(traceback.format_exc(),style="white")
    logger.print("Missing Module Not Using BDSupReader")
except Exception as E:
    BDSup=None
    logger.print(E)
    logger.print(traceback.format_exc(),style="white")
    logger.print("Error Not using BDSupReader")


    
try:
    import mediatools.PGSReader.imagemaker as imagemaker
    import mediatools.PGSReader.pgsreader as PGSReader
except ModuleNotFoundError:
    imagemaker=None
    PGSreader=None
    logger.print(E)
    logger.print(traceback.format_exc(),style="white")
    logger.print("Missing Module Not Using PGSReader")

except Exception as E:
    imagemaker=None
    PGSreader=None
    logger.print(E)
    logger.print(traceback.format_exc(),style="white")
    logger.print("Error Not using PGSReader")

BDSUPBool= (BDSup!=None)
PGSBool=(imagemaker!=None and PGSReader!=None)

def PGSFunc(supFile):
   
    t = PGSReader.PGSReader(supFile)
    i=0
    try:
        for i,ds in enumerate(t.iter_displaysets()):
            if ds.has_image==False:
                continue
            newImage=f"image{i}.png"
            pds = ds.pds[0]
            ods = ds.ods[0]
            img = imagemaker.make_image(ods, pds)
            img.convert('L').save(newImage)
            logger.logger.debug(f"Saving {newImage}\n")



    except Exception as E:
        logger.logger.debug(traceback.format_exc())
        logger.logger.debug(str(E))
        logger.print("Ignoring PGSReader Error Contining")
   



def BDSupFunc(supFile):
    t=BDSup.BDSupReader(supFile)
    i=0
    try:
        for r in t.subPictures:
            for image in r.imageList:
                i=i+1
                newImage=f"image{i}.png"
                image["data"].save(newImage)
                logger.logger.debug(f"Saving {newImage}\n")

    except Exception as E:
        logger.logger.debug(traceback.format_exc())
        logger.logger.debug(str(E))
        logger.print("Ignoring BDSup Error Contining")
  








def getSubImages(supFile):
    outputDir=os.path.join(os.path.abspath(f"./subImages"),f"{os.path.basename(supFile)}/")
    with dir.cwd(outputDir):
        if BDSUPBool:
            BDSupFunc(supFile)
        if PGSBool and len(os.listdir(outputDir))==0:
            PGSFunc(supFile)
        return outputDir
    





        