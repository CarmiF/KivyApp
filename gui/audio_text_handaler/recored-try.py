
import pyaudio
import wave
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

from .encryption import encryption_audio
def record_audio(self, new_sub_audio_path, key):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()

        while self.recording==True:
            data = stream.read(1024)
            frames.append(data)

            passed= time.time() - start
            secs= passed % 60
            mins = passed // 60 
            hours = mins // 60
            # self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
        
        stream.stop_stream()
        stream.close()
        audio.terminate()

        encrypted_audio_data = encrypt_audio_data(b''.join(frames), key)

        sound_file = wave.open(new_sub_audio_path,"wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(encrypted_audio_data))
        sound_file.close()
    

def encrypt_audio_data(self, audio_data, key):
        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_audio_data = encryptor.update(audio_data) + encryptor.finalize()
        return encrypted_audio_data

