# text_to_music.py | Dave Abel | Part of the ArtLanguage Project

from midiutil.MidiFile import MIDIFile
import sys
import re
import random

def add_note(song, pitch, time, duration = 0.5, volume = 80):
	# add the note.
	song.addNote(0,0,pitch,time,duration,volume)

def main():
	# Create the MIDIFile Object
	song = MIDIFile(1)

	if len(sys.argv) <= 1:
		print "Usage: python text_to_music.py <text_file>"
		quit()

	trackName = re.split("\.",sys.argv[1])[0]

	story = open("stories/" + trackName + ".txt", "r").read()

	storyChars = list(story.lower())

	time = 0
	duration = 0.5
	# Build a note
	for char in storyChars:
		pitch = 0
		if char in ["a","b","c","d","e","f","g"]:
			pitch = ord(char) - random.randint(35,45)
		else:
			volume = 0
		add_note(song, pitch, time, duration)
		time += duration

	# Add track name and tempo. The first argument to addTrackName and
	# addTempo is the time to write the event.
	track = 0
	time = 0
	song.addTrackName(track,time,trackName)
	song.addTempo(track,time, 120)

	# And write it to disk.
	binfile = open(trackName +".mid", 'wb')
	song.writeFile(binfile)
	binfile.close()

if __name__ == "__main__":
	main()