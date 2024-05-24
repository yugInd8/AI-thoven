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

def generate_melody(chord, duration):
    # Define melody notes based on the chord
    chord_notes = {
        "Cmaj7": ["C", "E", "G", "B"],
        "Fmaj7": ["F", "A", "C", "E"],
        "Dm7": ["D", "F", "A", "C"],
        "G7": ["G", "B", "D", "F"],
        "Am": ["A", "C", "E"],
        "Em7": ["E", "G", "B", "D"],
        "A7": ["A", "C#", "E", "G"],
    }
    return random.choice(chord_notes[chord]), duration

def generate_left_hand_melody(chord, duration):
    # Define left-hand melody notes based on the chord
    chord_notes = {
        "Cmaj7": ["C3", "E3", "G3", "B3"],
        "Fmaj7": ["F3", "A3", "C4", "E4"],
        "Dm7": ["D3", "F3", "A3", "C4"],
        "G7": ["G3", "B3", "D4", "F4"],
        "Am": ["A2", "C3", "E3"],
        "Em7": ["E2", "G2", "B2", "D3"],
        "A7": ["A2", "C#3", "E3", "G3"],
    }
    return random.choice(chord_notes.get(chord, ["C3"])), duration

def generate_midi(chord_progression, num_measures, tempo):
    # Create a MIDI file
    midi = MIDIFile(1)
    track = 0
    channel_right = 0
    channel_left = 1
    time = 0
    midi.addTempo(track, time, tempo)

    # Generate chord progression and melodies
    for measure in range(num_measures):
        for chord in chord_progression:
            duration = 4  # Each chord lasts for 4 beats (1 measure)
            for note in chord.split():
                midi.addNote(track, channel_right, note_to_midi_pitch(note), time, duration, 100)
                left_hand_note, _ = generate_left_hand_melody(chord, duration)
                midi.addNote(track, channel_left, note_to_midi_pitch(left_hand_note), time, duration, 100)

            melody_note, melody_duration = generate_melody(chord, duration)
            midi.addNote(track, channel_right, note_to_midi_pitch(melody_note), time, melody_duration, 100)

            time += duration

    # Save the MIDI file
    with open("recreational_music.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    # Convert note name to MIDI pitch
    note_values = {"C": 60, "C#": 61, "D": 62, "D#": 63, "E": 64, "F": 65, "F#": 66, "G": 67, "G#": 68, "A": 69, "A#": 70, "B": 71,
                   "Cm": 60, "C#m": 61, "Dm": 62, "D#m": 63, "Em": 64, "Fm": 65, "F#m": 66, "Gm": 67, "G#m": 68, "Am": 69, "A#m": 70, "Bm": 71,
                   "Cmaj7": 60, "C#maj7": 61, "Dmaj7": 62, "D#maj7": 63, "Emaj7": 64, "Fmaj7": 65, "F#maj7": 66, "Gmaj7": 67, "G#maj7": 68, "Amaj7": 69, "A#maj7": 70, "Bmaj7": 71,
                   "G7": 67, "G#7": 68, "A7": 69, "A#7": 70, "B7": 71, "C7": 72, "C#7": 73, "D7": 74, "D#7": 75, "E7": 76, "F7": 77, "F#7": 78}
    return note_values.get(note, 60)  # Default to 60 if note not found


if __name__ == "__main__":
    # Set parameters
    num_measures = 8  # Increase the number of measures for longer compositions
    tempo = 120

    # Generate chord progression and MIDI file
    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)
