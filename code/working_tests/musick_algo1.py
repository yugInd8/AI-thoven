from src.midiutil.MidiFile3 import MIDIFile
import random

MyMIDI = MIDIFile(1)

#A,F,G,E chords over 4
chordset_1 = [
    (57,60,64), 
    (53,57,60),
    (55,59,62),
    (52,55,59)
]

def playM(melody, base) :
    