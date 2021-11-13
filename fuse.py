from pydub import AudioSegment
import os

for firstId in range(1,152):
  os.mkdir(f"./fused/{firstId}")
  for secondId in range(1,152):
    firstCry = AudioSegment.from_mp3(f"./firsthalf/{firstId}.mp3")
    secondCry = AudioSegment.from_mp3(f"./secondhalf/{secondId}.mp3")
    fused = firstCry + secondCry
    fused.export(f"./fused/{firstId}/{firstId}.{secondId}.mp3", format="mp3")