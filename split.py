from pydub import AudioSegment

for id in range(1,152):
    curCry = AudioSegment.from_mp3(f"./cries/{id}.mp3")
    duration = curCry.duration_seconds * 500

    firsthalf = curCry[:duration]
    secondhalf = curCry[-duration:]
    firsthalf.export(f"./firsthalf/{id}.mp3", format="mp3")
    secondhalf.export(f"./secondhalf/{id}.mp3", format="mp3")