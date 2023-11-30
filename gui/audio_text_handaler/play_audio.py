

import pyaudio
import wave
import time

def play_wav(file_path):
    CHUNK = 1024

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    try:
        # Open the WAV file
        wf = wave.open(file_path, 'rb')

        # Open a stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Read data in chunks and play it
        data = wf.readframes(CHUNK)
        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # Wait for the sound to finish playing
        stream.stop_stream()
        stream.close()
        p.terminate()

    except IOError as e:
        print(f"Error: {e}")
    finally:
        p.terminate()