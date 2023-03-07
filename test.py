import os 
import simpleaudio as sa

os.chmod("test.py" , 0o755)

playlist = "C:/Users/hp/Desktop/gbedu/01 - Starboy (feat. Daft Punk).mp3"


wave_obj = sa.WaveObject.from_wave_file(playlist)
play_obj = wave_obj.play()
play_obj.wait_done()
# home_dir = os.path.expanduser("~\Music")

# rocks = os.listdir(home_dir)

# for files in rocks:
#     print(rocks)