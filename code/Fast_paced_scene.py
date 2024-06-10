#this is just a working example code, it hasn't been tuned to UX expectations yet

from src.midiutil.MidiFile3 import MIDIFile
import random

chord_progressions = [
    ["C", "Am", "F", "G"],
    ["Dm", "G", "C", "Am"],
    ["Em", "Am", "Dm", "G"],
]

chord_notes = {
    "C": ["C3", "E3", "G3"],
    "Am": ["A2", "C3", "E3"],
    "F": ["F2", "A2", "C3"],
    "G": ["G2", "B2", "D3"],
}

melody_notes = {
    "C": ["E4", "G4", "C5"],
    "Am": ["C4", "E4", "A4"],
    "F": ["A3", "C4", "F4"],
    "G": ["B3", "D4", "G4"],
}

def note_to_midi_pitch(note):
    note_values = {
        "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63,
        "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, "Ab": 68,
        "A": 69, "A#": 70, "Bb": 70, "B": 71, "Cb": 59,
        "Cm": 60, "C#m": 61, "Dbm": 61, "Dm": 62, "D#m": 63, "Ebm": 63,
        "Em": 64, "Fm": 65, "F#m": 66, "Gbm": 66, "Gm": 67, "G#m": 68, "Abm": 68,
        "Am": 69, "A#m": 70, "Bbm": 70, "Bm": 71, "Cbm": 59
    }
    return note_values.get(note, 60) 

def generate_melody(chord):
    return random.choice(melody_notes.get(chord, ["C"]))

def generate_music():
    midi = MIDIFile(1)
    track = 0
    channel = 0
    time = 0
    duration_per_chord = 4  # Each chord lasts for 4 beats (1 measure)
    tempo = 160  # Fast tempo

    midi.addTempo(track, time, tempo)

    chord_progression = random.choice(chord_progressions)

    for chord in chord_progression:
        for note in chord_notes.get(chord, []):
            midi.addNote(track, channel, note_to_midi_pitch(note), time, duration_per_chord, 100)

        melody_note = generate_melody(chord)
        midi.addNote(track, channel, note_to_midi_pitch(melody_note), time, duration_per_chord, 100)

        time += duration_per_chord

    with open("output.mid", "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    generate_music()
