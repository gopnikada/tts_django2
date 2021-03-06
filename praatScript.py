import subprocess
import pathlib

def generatePraatScriptText(path, origFileName, synthFileName, exportName):
    origFileNameArr = origFileName.split('.')
    synthFileNameArr = synthFileName.split('.')

    scText = f'Read from file: "{path}\\{synthFileNameArr[0]}.{synthFileNameArr[1]}"\n' \
             f'Read from file: "{path}\\{origFileNameArr[0]}.{origFileNameArr[1]}"\n' \
             f'To Manipulation: 0.01, 75, 600\n' \
             f'Extract pitch tier\n' \
             f'selectObject: "Sound {synthFileNameArr[0]}"\n' \
             f'To Manipulation: 0.01, 75, 600\n' \
             f'selectObject: "PitchTier {origFileNameArr[0]}"\n' \
             f'plusObject: "Manipulation {synthFileNameArr[0]}"\n' \
             f'Replace pitch tier\n' \            
             f'selectObject: "Manipulation {synthFileNameArr[0]}"\n' \
             f'Get resynthesis (overlap-add)\n' \
             f'Save as WAV file: "{path}\\{exportName}"\n'
    return scText



def createPraatFile(scTextArg, scriptFileName):
    linesArr = scTextArg.split("\n")
    for i in range(0, len(linesArr) - 1):
        writeToFile = f'echo {linesArr[i]}>> {scriptFileName}'
        res = subprocess.call(writeToFile, shell=True)
        if res == 1:
            raise ValueError('A very specific bad thing happened.')

#res = subprocess.call(f'praat --run "{scriptFileName}"', shell=True)  # 1 - error, 0 - ok
#if res == 1:
#    raise ValueError('A very specific bad thing happened.')


