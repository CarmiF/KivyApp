from kivy.metrics import dp
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os

# from .utils.utils_main import 
from .audio_text_handaler.play_audio import play_wav

class ViewRecordingPopup(App):
    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
        self.build()
    
    def build(self):
        main_path = os.path.join(self.definitions.recorded_data_path, str(self.definitions.btn_text))
        audioPath = os.path.join(main_path, "audio.wav")
        textPath = os.path.join(main_path, "text.txt")
        
        # Use relative sizes for layout
        popup_content = BoxLayout(orientation='vertical')
        
        play_audio_btn = Button(text='Play Recording')
        play_audio_btn.bind(on_release=lambda _: play_wav(audioPath))
        
        file_content = ""
        if os.path.exists(textPath):
            with open(textPath, "r") as file:
                file_content = str(file.read())
        
        popup_content.add_widget(play_audio_btn)
        
        # Use relative sizes for Label
        text_label = Label(
            text=file_content
            
        )
        
        popup_content.add_widget(text_label)
        
        # Create Popup with content
        self.popup = Popup(title=str(self.definitions.btn_text), content=popup_content, size_hint=(None, None), size=(400, 300), auto_dismiss=True)
        self.popup.open()

# Note: dp() is now imported from kivy.metrics
