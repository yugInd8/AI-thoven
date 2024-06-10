from src.midiutil.MidiFile3 import MIDIFile

# create the MIDIFile object with 1 track
midi = MIDIFile(1)

# add the track name and tempo
midi.addTrackName(0, 0, "My Simple Tune")
midi.addTempo(0, 0, 120)

# create a list of notes and durations to add to the track
notes = [60, 62, 64, 65, 67, 69, 71]
durations = [1, 0.5, 0.25, 1, 0.75, 0.5, 2]

# use a for loop to add each note to the track
for i, (note, duration) in enumerate(zip(notes, durations)):
   # add the note on event
   midi.addNote(0, 0, note, i, duration, 100)
   # add the note off event
   midi.addNote(0, 0, note, i+duration, duration, 0)

# write the MIDIFile to a file
with open("simple_tune.mid", "wb") as output_file:
   midi.writeFile(output_file)