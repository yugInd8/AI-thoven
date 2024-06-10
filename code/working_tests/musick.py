#Import the library
from src.midiutil.MidiFile3 import MIDIFile

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time, 120)

# Add a note. addNote expects the following information:
channel = 0
duration = 1
volume = 100

#will be replaced by algorithms based on music theory
MyMIDI.addNote(track,channel,69,0,duration,volume)
MyMIDI.addNote(track,channel,72,0.5,duration,volume)
MyMIDI.addNote(track,channel,88,1,duration,volume)
MyMIDI.addNote(track,channel,66,1.5,duration,volume)
MyMIDI.addNote(track,channel,69,2,duration,volume)
MyMIDI.addNote(track,channel,85,2.5,duration,volume)
MyMIDI.addNote(track,channel,63,3,duration,volume)
MyMIDI.addNote(track,channel,66,3.5,duration,volume)
MyMIDI.addNote(track,channel,82,4,duration,volume)

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

