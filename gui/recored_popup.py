
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import threading

from .utils.utils_main import get_new_subfolder_path
from .audio_text_handaler.recored import record_audio
from .audio_text_handaler.transcribe import transcribe_audio

class RecordPopup(App):

    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions

    def record_popup_pressed(self, touch):
        print("recored_button_pressed")
        if self.recording:
            self.recording=False
            self.message_button.text="Record"
            print(self)
        else:
            self.recording=True
            threading.Thread(target=self.recored_thread).start()
            self.message_button.text="Recording- Press to stop"

    def recored_thread(self):
        new_sub_audio_path, new_sub_text_path = get_new_subfolder_path(self.definitions.recorded_data_path)
        if self.definitions.recored==True: record_audio(self, new_sub_audio_path)
        if self.definitions.transcribe==True: transcribe_audio(new_sub_audio_path, new_sub_text_path)
        self.recording = False
        self.message_button.text="Record"
    
    def build(self):
        self.popup_content = BoxLayout(orientation='vertical', spacing=10)
        self.message_button = Button(text="Record")
        self.recording= False
        self.message_button.bind(on_release= self.record_popup_pressed)
        self.popup_content.add_widget(self.message_button)
        self.popup = Popup(title="", content=self.popup_content, size_hint=(None, None), size=(300, 200))
        self.popup.open()
