import whisper

def transcribe_audio(file_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    transcription = model.transcribe(file_path)
    return transcription['text']

if __name__ == '__main__':
    audio_file = "path_to_your_audio.wav"  # Update this with your audio file path
    print(transcribe_audio(audio_file))