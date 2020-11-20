# check python version, this script requires python3
import sys
if sys.version_info[0] < 3:
    print('ERROR: This script requires Python 3')
    sys.exit(1)

import os
import subprocess    
from argparse import ArgumentParser


# ################################ #  
#           Main Program           #
# ################################ #

# argument parsing

parser = ArgumentParser(description="Simple script that turns a series of turntable images in a given directory into a little .mov clip, using ffmpeg", epilog="")

parser.add_argument("inputDir",  help="input directory of images (must be PNG files)")

pArgs     = parser.parse_args()
inputDir  = vars(pArgs)["inputDir"]

inputFileList = os.listdir(inputDir)

# TODO: could do some sanity checks here
#       for now, we assume the directory contains PNG files with the correct filenames & number padding
numDigits = 1
for inputFile in inputFileList:
    inputFileName = inputFile[0:inputFile.rfind('.')]
    numDigits = len(inputFileName)
    break
    
# run ffmpeg

cmdline = ['ffmpeg', '-framerate', '60', '-i', './' + inputDir + '/%0' + str(numDigits) + 'd.png', '-vcodec', 'png', inputDir + '.mov']
print(cmdline)
try:
    subprocess.check_output(cmdline)
except Exception as e:
    print("******************************************************************")
    print(" - Error: {0}".format(e))
    print("******************************************************************")
    
