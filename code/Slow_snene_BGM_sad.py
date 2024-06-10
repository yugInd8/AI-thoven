#this is just a working example code, it hasn't been tuned to UX expectations yet

from src.midiutil.MidiFile3 import MIDIFile
import random

def generate_chord_progression(num_chords):
    chord_progressions = [
        ["Cmaj7", "Fmaj7", "Dm7", "G7"],
        ["Am", "Dm7", "G7", "Cmaj7"],
        ["Fmaj7", "G7", "Cmaj7", "Am"],
        ["Em7", "A7", "Dm7", "G7"],
    ]
    
    chord_progressions *= num_chords // len(chord_progressions)
    remainder = num_chords % len(chord_progressions)
    chord_progression = chord_progressions[:remainder] + chord_progressions
    
    return chord_progression

def generate_melody(chord):
    chord_notes = {
        "Cmaj7": ["E5", "G5", "B5"],
        "Fmaj7": ["A5", "C6", "E6"],
        "Dm7": ["F5", "A5", "C6"],
        "G7": ["B5", "D6", "F6"],
        "Am": ["C5", "E5", "A5"],
        "Em7": ["G5", "B5", "D6"],
        "A7": ["C#5", "E5", "G#5"],
    }
    if isinstance(chord, list):  # checks if chord is a chord progression
        return [random.choice(chord_notes[c]) for c in chord]
    else:
        return random.choice(chord_notes[chord])

def generate_left_hand_chord(chord):
    chord_notes = {
        "Cmaj7": ["C3", "E3", "G3", "B3"],
        "Fmaj7": ["F3", "A3", "C4", "E4"],
        "Dm7": ["D3", "F3", "A3", "C4"],
        "G7": ["G3", "B3", "D4", "F4"],
        "Am": ["A2", "C3", "E3", "A3"],
        "Em7": ["E2", "G2", "B2", "D3"],
        "A7": ["A2", "C#3", "E3", "G#3"],
    }
    if isinstance(chord, list):  # Check if chord is a chord progression
        return [chord_notes.get(c, []) for c in chord]
    else:
        return chord_notes.get(chord, [])

def generate_midi(chord_progression, num_measures, tempo):
    midi = MIDIFile(1)
    track = 0
    channel_right = 0
    channel_left = 1
    time = 0
    midi.addTempo(track, time, tempo)

    for chord in chord_progression:
        left_hand_chord = generate_left_hand_chord(chord)
        melody_notes = [generate_melody(chord) for _ in range(3)]  # 3 melody notes per chord
        duration = 4  # Each chord lasts for 4 beats (1 measure)
        
        if left_hand_chord:
            for notes in left_hand_chord:
                for note in notes:
                    midi.addNote(track, channel_left, note_to_midi_pitch(note), time, duration, 100)
        
        for note in melody_notes:
            midi.addNote(track, channel_right, note_to_midi_pitch(note), time, 2, 100)  # Melody note duration is 2 beats
            
            time += 2
        
        time += 2  
    with open("output.mid", "wb") as f:
        midi.writeFile(f)

def note_to_midi_pitch(note):
    note_values = {"C2": 48, "C#2": 49, "D2": 50, "D#2": 51, "E2": 52, "F2": 53, "F#2": 54, "G2": 55, "G#2": 56, "A2": 57, "A#2": 58, "B2": 59,
                   "C3": 60, "C#3": 61, "D3": 62, "D#3": 63, "E3": 64, "F3": 65, "F#3": 66, "G3": 67, "G#3": 68, "A3": 69, "A#3": 70, "B3": 71,
                   "C4": 72, "C#4": 73, "D4": 74, "D#4": 75, "E4": 76, "F4": 77, "F#4": 78, "G4": 79, "G#4": 80, "A4": 81, "A#4": 82, "B4": 83,
                   "C5": 84, "C#5": 85, "D5": 86, "D#5": 87, "E5": 88, "F5": 89, "F#5": 90, "G5": 91, "G#5": 92, "A5": 93, "A#5": 94, "B5": 95}
    return note_values.get(note, 60)  # Default to 60 if note not found

if __name__ == "__main__":
    num_measures = 16  # 16 measures for one minute
    tempo = 140  # Adjust tempo as needed for soothing music

    chord_progression = generate_chord_progression(num_measures)
    generate_midi(chord_progression, num_measures, tempo)
