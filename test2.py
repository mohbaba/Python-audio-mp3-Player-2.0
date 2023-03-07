import os
import pygame
from pydub import AudioSegment

# set up Pygame
pygame.init()
pygame.mixer.init()

# define function to play audio using Pygame
def play_audio_pygame(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

# define function to play audio using Pydub
def play_audio_pydub(filename):
    sound = AudioSegment.from_file(filename)
    raw_data = sound.raw_data
    sample_width = sound.sample_width
    frame_rate = sound.frame_rate
    num_channels = sound.channels
    pygame.mixer.Sound(buffer=raw_data).play()

# loop through files in folder and play each one
folder_path = "/path/to/folder"

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        # use Pygame to play MP3 files
        file_path = os.path.join(folder_path, filename)
        play_audio_pygame(file_path)
    else:
        # use Pydub to convert non-MP3 files to WAV and play with Pygame
        file_path = os.path.join(folder_path, filename)
        sound = AudioSegment.from_file(file_path)
        sound.export("temp.wav", format="wav")
        play_audio_pygame("temp.wav")

    # wait for audio to finish playing before moving on to the next file
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
        
        
        
# Note that this code uses Pygame to play MP3 files directly, but for other file types it first uses Pydub to convert them to WAV format and then plays them with Pygame. It also waits for each audio file to finish playing before moving on to the next one. You can adjust the folder path as needed to target the folder with your audio files.