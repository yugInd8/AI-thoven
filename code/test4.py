from src.midiutil.MidiFile3 import MIDIFile

# create the MIDIFile object with 2 tracks
midi = MIDIFile(2)

# add the track names and tempo
midi.addTrackName(0, 0, "Right Hand")
midi.addTrackName(1, 0, "Left Hand")
midi.addTempo(0, 0, 120)

# set the instrument for each track
midi.addProgramChange(0, 0, 0, 74)  # flute for right hand track
midi.addProgramChange(1, 0, 0, 74)  # flute for left hand track

# create a list of notes, durations, and volumes for the right hand part
right_notes = [60, 62, 64, 65, 67, 69, 71]
right_durations = [1, 0.5, 0.25, 1, 0.75, 0.5, 2]
right_volumes = [100, 80, 60, 50, 40, 30, 20]

# create a list of notes, durations, and volumes for the left hand part
left_notes = [48, 50, 52, 53, 55, 57, 59]
left_durations = [1, 0.5, 0.25, 1, 0.75, 0.5, 2]
left_volumes = [100, 80, 60, 50, 40, 30, 20]

# initialize a variable to keep track of the total time elapsed
total_time = 0

# use a for loop to add each note to the right hand track
for i, (note, duration, volume) in enumerate(zip(right_notes, right_durations, right_volumes)):
   # add the note with the specified duration and volume starting at the current total time
   midi.addNote(0, 0, note, total_time, duration, volume)
   # increment the total time by the duration of the current note
   total_time += duration

# reset the total time to 0 for the left hand track
total_time = 0

# use a for loop to add each note to the left hand track
for i, (note, duration, volume) in enumerate(zip(left_notes, left_durations, left_volumes)):
   # add the note with the specified duration and volume starting at the current total time
   midi.addNote(1, 0, note, total_time, duration, volume)
   # increment the total time by the duration of the current note
   total_time += duration

# write the MIDIFile to a file
with open("piano_song.mid", "wb") as output_file:
   midi.writeFile(output_file)