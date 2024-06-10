from src.midiutil.MidiFile3 import MIDIFile

import random

def generate_chord_progression(num_chords):
    # Define chord progressions - You can create your own chord progressions or use libraries like music21
    chord_progressions = [
        ["C", "Am", "F", "G"],
        ["Dm", "G", "C", "Am"],
        ["Em", "Am", "Dm", "G"],
        # Add more chord progressions as needed
    ]
    return random.choice(chord_progressions)[:num_chords]

def generate_melody(chord, duration):
    # Define melody notes based on the chord
    chord_notes = {
        "C": ["C", "E", "G"],
        "Dm": ["D", "F", "A"],
        "Em": ["E", "G", "B"],
        "F": ["F", "A", "C"],
        "G": ["G", "B", "D"],
        "Am": ["A", "C", "E"],
        # Add more chords and their notes as needed
    }
    return random.choice(chord_notes[chord]), duration

def generate_midi(chord_progression, num_measures, tempo):
    # Create a MIDI file
    midi = MIDIFile(1)
    track = 0
    channel = 0
    time = 0
    midi.addTempo(track, time, tempo)

    # Generate chord progression and melody
    for measure in range(num_measures):
        for chord in chord_progression:
            duration = 4  # Each chord lasts for 4 beats (1 measure)
            for note in chord.split():
                midi.addNote(track, channel, note_to_midi_pitch(note), time, duration, 100)

            melody_note, melody_duration = generate_melody(chord, duration)
            midi.addNote(track, channel, note_to_midi_pitch(melody_note), time, melody_duration, 100)

            time += duration

    # Save the MIDI file
    with open("generated_music.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    # Convert note name to MIDI pitch
    note_values = {"C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65, "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71,
                   "Cm": 60, "C#m": 61, "Dm": 62, "D#m": 63, "Em": 64, "Fm": 65, "F#m": 66, "Gm": 67, "G#m": 68, "Am": 69, "A#m": 70, "Bm": 71}
    return note_values[note]


if __name__ == "__main__":
    # Set parameters
    num_measures = 4
    tempo = 120

    # Generate chord progression and MIDI file
    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)