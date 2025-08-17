from flask import Flask, render_template, request, send_file, jsonify
from google.cloud import texttospeech
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']
    voice_name = request.form['voice']
    rate = float(request.form.get('rate', 1.0))
    pitch = float(request.form.get('pitch', 0.0))

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-XA",
        name=voice_name
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=rate,
        pitch=pitch
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Ensure static directory exists
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    filename = f"output_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(static_dir, filename)
    with open(filepath, "wb") as out:
        out.write(response.audio_content)

    return jsonify({"audio_url": f"/static/{filename}"})

if __name__ == "__main__":
    app.run(debug=True)