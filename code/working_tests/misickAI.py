import openai
from src.midiutil.MidiFile3 import MIDIFile
import os

# Function to generate music sequence using ChatGPT API
def generate_music_sequence(prompt):
    openai.api_key = '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'
    response = openai.completions.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

# Create a MIDI file and add notes
def create_midi_from_sequence(sequence):
    MyMIDI = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    duration = 1
    volume = 100
    pitch = 60  # Starting pitch (adjust as needed)
    for note in sequence.split():
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)
        pitch += int(note)  # Increment pitch based on the generated note
        time += duration
    return MyMIDI

# Write MIDI file and play it
def write_and_play_midi(midi_data, filename="output.mid"):
    with open(filename, 'wb') as binfile:
        midi_data.writeFile(binfile)
    binfile.close()
    #os.system("your_midi_player_command " + filename)  # Replace with your MIDI player command

# Example usage
    
prompt = "Generate a music sequence:"
generated_sequence = generate_music_sequence(prompt)
print("Generated Music Sequence:", generated_sequence)
midi_data = create_midi_from_sequence(generated_sequence)
write_and_play_midi(midi_data)
