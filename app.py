import os
from flask import Flask, render_template, request, send_file
from google.cloud import texttospeech

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    error = None
    if request.method == 'POST':
        text = request.form.get('text')
        voice = request.form.get('voice')
        speed = float(request.form.get('speed', 1.0))
        pitch = float(request.form.get('pitch', 0.0))
        if not text:
            error = "الرجاء إدخال نص."
        else:
            try:
                client = texttospeech.TextToSpeechClient()
                synthesis_input = texttospeech.SynthesisInput(text=text)
                voice_params = texttospeech.VoiceSelectionParams(
                    language_code="ar-XA",
                    name=voice
                )
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3,
                    speaking_rate=speed,
                    pitch=pitch
                )
                response = client.synthesize_speech(
                    input=synthesis_input,
                    voice=voice_params,
                    audio_config=audio_config
                )
                filename = "output.mp3"
                with open(filename, "wb") as out:
                    out.write(response.audio_content)
                audio_file = filename
            except Exception as e:
                error = "حدث خطأ أثناء تحويل النص إلى صوت: " + str(e)
    return render_template('index.html', audio_file=audio_file, error=error)

@app.route('/download')
def download():
    filename = "output.mp3"
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    return "لا يوجد ملف صوتي."

if __name__ == '__main__':
    app.run(debug=True)