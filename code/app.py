from flask import Flask, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

def generate_midi(script_name):
    subprocess.run(['python3', f'{script_name}.py'])
    return send_file('output.mid', mimetype='audio/midi')

@app.route('/protagonist-bgm')
def protagonist_bgm():
    return generate_midi('Protagonist_BGM')

@app.route('/antagonist-bgm')
def antagonist_bgm():
    return generate_midi('Antagonist_BGM')

@app.route('/slow-scene-sad')
def slow_scene_sad():
    return generate_midi('Slow_scene_BGM_sad')

@app.route('/slow-scene-happy')
def slow_scene_happy():
    return generate_midi('Slow_scene_BGM_happy')

@app.route('/fast-paced-scene')
def fast_paced_scene():
    return generate_midi('Fast_paced_scene')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
