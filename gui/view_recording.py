from kivy.app import App
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os

from .utils.utils_main import *
from .audio_text_handaler.play_audio import play_wav

class ViewRecordingPopup(App):
    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
        self.build()
    
    def build(self):
        main_path = os.path.join(self.definitions.recorded_data_path, str(self.definitions.btn_text))
        audioPath = os.path.join(main_path ,"audio.wav")
        textPath = os.path.join(main_path , "text.txt")
        popup_content = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.8, 0.7))
        play_audio_btn = Button(text = 'play recording', size_hint_y=None, height=40)
        play_audio_btn.bind(on_release= lambda _:play_wav(audioPath))
        file_content =""
        if os.path.exists(textPath):        
            with open(textPath, "r") as file:
                file_content = str(file.read())

        popup_content.add_widget(play_audio_btn)
        text_label = Label(
                text=file_content,
                size_hint_y=None,
                height=40,
                text_size=(400, None),  # Set the width for text wrapping
                halign='left',
                valign='top'
            )
        
        popup_content.add_widget(text_label)
        self.popup = Popup(title=str(self.definitions.btn_text), content=popup_content, size_hint=(0.8, 0.7))
        self.popup.open()