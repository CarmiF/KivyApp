
import speech_recognition as sr


def transcribe_audio(newSubAudioPath, newSubTextPath ):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(newSubAudioPath) as source:
        audio = recognizer.record(source)

    # Transcribe the audio to text
    try:
        text = recognizer.recognize_google(audio)
        
        file_path= newSubTextPath
        print("Transcribe3")

        with open(file_path, 'w') as file:
                file.write(text)            
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Error: {0}".format(e)