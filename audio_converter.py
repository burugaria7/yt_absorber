# -*- coding: utf-8 -*-
import pydub
import glob

files = glob.glob("./mp3/*")
for file in files:
    print(file[6:-8])
    sound = pydub.AudioSegment.from_mp3(file)
    sound.export("./wav/"+file[6:-8]+".wav", format="wav")
# sound = pydub.AudioSegment.from_mp3("input.mp3")
# sound.export("output.wav", format="wav")