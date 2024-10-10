import time
import re
import pygame

def load_lyrics(filename):
    lyrics = []
    with open(filename, 'r') as f:
        for line in f:
            # Use regex to find the timestamp and text
            match = re.match(r'\[(\d{2}):(\d{2}\.\d{2})\](.*)', line)
            if match:
                minutes, seconds, text = match.groups()
                timestamp = int(minutes) * 60 + float(seconds)
                lyrics.append((timestamp, text.strip()))
    return lyrics

def display_lyrics(lyrics):
    start_time = time.time()
    for timestamp, line in lyrics:
        # Wait until it's time to display the next line
        while time.time() - start_time < timestamp:
            time.sleep(0.1)  # Sleep for a short while to avoid busy waiting
        print(line)

def main():
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load music and lyrics
    music_file = 'music.mp3'  # Path to your song
    lyrics_file = 'lyrics.lrc'  # Path to your LRC file

    # Load lyrics
    lyrics = load_lyrics(lyrics_file)

    # Load and play the music
    print("Playing music...")
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

    # Display the lyrics
    print("Displaying lyrics...")
    display_lyrics(lyrics)

    # Wait until the music is done
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print("Finished playing.")

if __name__ == "__main__":
    main()
