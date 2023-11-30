
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window  # Import the Window class
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import the Window class
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from .utils.utils_main import *
from .audio_text_handaler.play_audio import play_wav
from .view_recording import ViewRecordingPopup


import os




# def show_histoy_pupup(self):
#     print(self.data_folder_names)
#     data_folder_names= self.data_folder_names
#     get_recorded_data_path= self.get_recorded_data_path
#     self.history_popup = HistoryPopup().build(self)
#     self.history_popup.open()


class HistoryPopup(App):
    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
    
    def build(self):
        # popup_content = BoxLayout(orientation='vertical', spacing=10)
        box = GridLayout(cols=1, spacing=10, size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
        # print(self.main_array.data_folder_names)
        self.data_folder_names = sort_folders_by_date(self.definitions.recorded_data_path)
        for folder_name in self.data_folder_names:
            btn = Button(text=folder_name, size_hint_y=None, height=40)
            btn.bind(on_release= self.recorded_button_pressed)
            box.add_widget(btn)

        root = ScrollView(size_hint=(1, 0.9), size=(Window.width, Window.height))
        root.scroll_timeout = 250
        root.scroll_distance = 20
        root.add_widget(box)
        self.popup = Popup(title="Chocse the rec", content=root, size_hint=(0.8, 0.7))
        self.popup.open()

    def recorded_button_pressed(self, instance):
        
        self.definitions.btn_text = instance.text
        ViewRecordingPopup(self.definitions)
        
        print(instance.text)