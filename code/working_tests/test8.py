from src.midiutil.MidiFile3 import MIDIFile
import random

def generate_chord_progression(num_chords):
    # Define complex chord progressions inspired by classical music
    chord_progressions = [
        ["Cmaj7", "Fmaj7", "Dm7", "G7"],
        ["Am", "Dm7", "G7", "Cmaj7"],
        ["Fmaj7", "G7", "Cmaj7", "Am"],
        ["Em7", "A7", "Dm7", "G7"],
    ]
    return random.choice(chord_progressions)[:num_chords]

def generate_melody(chord):
    # Define melody notes based on the chord
    chord_notes = {
        "Cmaj7": ["E4", "G4", "B4"],
        "Fmaj7": ["A4", "C5", "E5"],
        "Dm7": ["F4", "A4", "C5"],
        "G7": ["B4", "D5", "F5"],
        "Am": ["C4", "E4", "A4"],
        "Em7": ["G4", "B4", "D5"],
        "A7": ["C#4", "E4", "G#4"],
    }
    return random.choice(chord_notes[chord])

def generate_left_hand_chord(chord):
    # Define left-hand chord notes based on the chord
    chord_notes = {
        "Cmaj7": ["C3", "E3", "G3", "B3"],
        "Fmaj7": ["F3", "A3", "C4", "E4"],
        "Dm7": ["D3", "F3", "A3", "C4"],
        "G7": ["G3", "B3", "D4", "F4"],
        "Am": ["A2", "C3", "E3", "A3"],
        "Em7": ["E2", "G2", "B2", "D3"],
        "A7": ["A2", "C#3", "E3", "G#3"],
    }
    return chord_notes[chord]

def generate_midi(chord_progression, num_measures, tempo):
    # Create a MIDI file
    midi = MIDIFile(1)
    track = 0
    channel_right = 0
    channel_left = 1
    time = 0
    midi.addTempo(track, time, tempo)

    # Generate chord progression and melodies
    for chord in chord_progression:
        left_hand_chord = generate_left_hand_chord(chord)
        melody_notes = [generate_melody(chord) for _ in range(4)]  # 3 melody notes per chord
        duration = 4  # Each chord lasts for 4 beats (1 measure)
        
        # Add left-hand chord
        for note in left_hand_chord:
            midi.addNote(track, channel_left, note_to_midi_pitch(note), time, duration, 100)
        
        # Add melody notes
        for note in melody_notes:
            midi.addNote(track, channel_right, note_to_midi_pitch(note), time, 2, 100)  # Melody note duration is 2 beats
            
            # Move to next melody note after 2 beats
            time += 1.5
        
        time += 1.5  # Move to the next chord after 2 beats of rest

    # Save the MIDI file
    with open("piano_piece.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    # Convert note name to MIDI pitch
    note_values = {"C2": 48, "C#2": 49, "D2": 50, "D#2": 51, "E2": 52, "F2": 53, "F#2": 54, "G2": 55, "G#2": 56, "A2": 57, "A#2": 58, "B2": 59,
                   "C3": 60, "C#3": 61, "D3": 62, "D#3": 63, "E3": 64, "F3": 65, "F#3": 66, "G3": 67, "G#3": 68, "A3": 69, "A#3": 70, "B3": 71,
                   "C4": 72, "C#4": 73, "D4": 74, "D#4": 75, "E4": 76, "F4": 77, "F#4": 78, "G4": 79, "G#4": 80, "A4": 81, "A#4": 82, "B4": 83,
                   "C5": 84, "C#5": 85, "D5": 86, "D#5": 87, "E5": 88, "F5": 89, "F#5": 90, "G5": 91, "G#5": 92, "A5": 93, "A#5": 94, "B5": 95}
    return note_values[note]


if __name__ == "__main__":
    # Set parameters
    num_measures = 8  # 8 for longer compositions
    tempo = 120

    # Generate chord progression and MIDI file
    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)
