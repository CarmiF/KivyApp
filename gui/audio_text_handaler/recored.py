
import pyaudio
import wave
import time

    
def record_audio(self, new_sub_audio_path):
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

        sound_file = wave.open(new_sub_audio_path,"wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
    



