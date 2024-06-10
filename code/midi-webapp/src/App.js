import React from 'react';
import * as Tone from 'tone';
import { Midi } from '@tonejs/midi';
import './App.css';  // Import the CSS file

function App() {
  const playMIDI = async (url) => {
    console.log(`Button clicked, fetching MIDI file from ${url}...`);
    await Tone.start();
    console.log('AudioContext started');

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      console.log('MIDI file fetched successfully');

      const arrayBuffer = await response.arrayBuffer();
      console.log('ArrayBuffer received');

      const midi = new Midi(arrayBuffer);
      console.log('MIDI parsed', midi);

      midi.tracks.forEach(track => {
        const synth = new Tone.PolySynth(Tone.Synth).toDestination();
        track.notes.forEach(note => {
          synth.triggerAttackRelease(
            note.name,
            note.duration,
            note.time + Tone.now(),
            note.velocity
          );
        });
      });

      console.log('Playing audio...');
    } catch (error) {
      console.error('Error fetching or parsing MIDI file:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Generate and Play MIDI Files</h1>
        <button onClick={() => playMIDI('http://127.0.0.1:5000/protagonist-bgm')}>Protagonist BGM</button>
        <button onClick={() => playMIDI('http://127.0.0.1:5000/antagonist-bgm')}>Antagonist BGM</button>
        <button onClick={() => playMIDI('http://127.0.0.1:5000/slow-scene-sad')}>Slow Scene BGM (Sad)</button>
        <button onClick={() => playMIDI('http://127.0.0.1:5000/slow-scene-happy')}>Slow Scene BGM (Happy)</button>
        <button onClick={() => playMIDI('http://127.0.0.1:5000/fast-paced-scene')}>Fast Paced Scene</button>
      </header>
    </div>
  );
}

export default App;
