from src.midiutil.MidiFile3 import MIDIFile

import random

def generate_chord_progression(num_chords):
    # chord progressions
    chord_progressions = [
        ["C", "G7", "C"],
        ["F", "C", "G7", "C"],
        ["G7", "C", "G7", "C"],
        ["C", "F", "G7", "C"],
    ]
    return random.choice(chord_progressions)[:num_chords]

def generate_melody(chord, duration):
    # melody notes based on the chord
    chord_notes = {
        "C": ["C", "E", "G"],
        "F": ["F", "A", "C"],
        "G7": ["F", "G", "B", "D"],
    }
    return random.choice(chord_notes[chord]), duration

def generate_midi(chord_progression, num_measures, tempo):
    midi = MIDIFile(1)
    track = 0
    channel = 0
    time = 0
    midi.addTempo(track, time, tempo)

    for measure in range(num_measures):
        for chord in chord_progression:
            duration = 4  # each chord lasts for 4 beats (1 measure)
            for note in chord.split():
                midi.addNote(track, channel, note_to_midi_pitch(note), time, duration, 100)

            melody_note, melody_duration = generate_melody(chord, duration)
            midi.addNote(track, channel, note_to_midi_pitch(melody_note), time, melody_duration, 100)

            time += duration

    with open("beethoven_inspired_music.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    note_values = {"C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65, "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71,
                   "Cm": 60, "C#m": 61, "Dm": 62, "D#m": 63, "Em": 64, "Fm": 65, "F#m": 66, "Gm": 67, "G#m": 68, "Am": 69, "A#m": 70, "Bm": 71,
                   "G7": 66}  # G7 added with pitch value, errors aarhe the in eg 11
    return note_values[note]

if __name__ == "__main__":
    num_measures = 8 
    tempo = 120

    # generate chord progression and MIDI file
    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)
