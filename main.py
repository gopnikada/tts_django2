#from moviepy.editor import *
from os import walk
import uuid
import os

# filesInDir = next(walk("C:\\Users\\49157\\Pictures\Camera Roll"), (None, None, []))[2]
# len = len(filesInDir)
# someFile = filesInDir[5]

#audioclip = AudioFileClip("C:\\Users\\49157\\Pictures\Camera Roll\\vid1.mp4")
#audioclip.write_audiofile("C:\\Users\\49157\\Pictures\Camera Roll\\audio.wav", fps=None, nbytes=2, buffersize=2000,
                       # codec=None, bitrate=None, ffmpeg_params=None,
                       # write_logfile=False, verbose=True, logger='bar')

#sessionId = str(uuid.uuid1())
#os.mkdir("C:\Kirill\Prog\FilesuploadProject\StoredFiles\\" + sessionId)
#import librosa as librosa
#
# from deep_translator import *
# translated = GoogleTranslator(source='auto', target='uk').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
# print(translated)
#
# import pathlib
# Rootpath = pathlib.Path().resolve()
# path = pathlib.Path().resolve().joinpath('models')
# sttModelPath = Rootpath.joinpath('models').joinpath('STT').joinpath('model.tflite')
# print(sttModelPath)


# videoclip = VideoFileClip(videoPath)
# audioclip_adjusted = AudioFileClip(adjustedPath)
# videoclip_changed_audio = videoclip.set_audio(audioclip_adjusted)

import pysrt
# from pysubparser import parser
#
# subtitles = parser.parse('./subs.srt')
#
# for subtitle in subtitles:
#     print(subtitle)
subs = pysrt.open('D:\\Proj\\Python\\MasterApp\\TTS\\subs.srt', encoding='utf-8')
subsText = subs.text.replace('\n', ' ')
for sub in subs.data:
    print(sub)


