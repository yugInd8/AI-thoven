#this is just a working example code, it hasn't been tuned to UX expectations yet

from src.midiutil.MidiFile3 import MIDIFile
import random

def generate_chord_progression(num_chords):
    chord_progressions = [
        ["C", "Am", "F", "G"],
        ["Dm", "G", "C", "Am"],
        ["Em", "Am", "Dm", "G"],
    ]
    return random.choice(chord_progressions)[:num_chords]

def generate_melody(chord, duration):
    #melody notes tailored for the specific chords
    chord_notes = {
        "C": ["E5", "G#5", "B5"],
        "Dm": ["D5", "F5", "A5"],
        "Em": ["E5", "G5", "B5"],
        "F": ["F5", "A5", "C6"],
        "G": ["G5", "B5", "D6"],
        "Am": ["A4", "C5", "E5"],
    }
    return random.choice(chord_notes.get(chord, ["C5", "E5", "G5"])), duration


def generate_midi(chord_progression, num_measures, tempo):
    midi = MIDIFile(1)
    track = 0
    channel = 0
    time = 0
    midi.addTempo(track, time, tempo)

    for measure in range(num_measures):
        for chord in chord_progression:
            duration = 1  # Each chord lasts for 1 beat
            for note in chord.split():
                midi.addNote(track, channel, note_to_midi_pitch(note), time, duration, 100)

            melody_note, melody_duration = generate_melody(chord, duration)
            midi.addNote(track, channel, note_to_midi_pitch(melody_note), time, melody_duration, 100)

            time += duration

    with open("output.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    #note name mapped to MIDI pitch
    note_values = {
        "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63,
        "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, "Ab": 68,
        "A": 69, "A#": 70, "Bb": 70, "B": 71, "Cb": 59,
        "Cm": 60, "C#m": 61, "Dbm": 61, "Dm": 62, "D#m": 63, "Ebm": 63,
        "Em": 64, "Fm": 65, "F#m": 66, "Gbm": 66, "Gm": 67, "G#m": 68, "Abm": 68,
        "Am": 69, "A#m": 70, "Bbm": 70, "Bm": 71, "Cbm": 59
    }
    return note_values.get(note, 60)  #default value is 60 (C4) if note is not found


if __name__ == "__main__":
    num_measures = 4
    tempo = 120

    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)
