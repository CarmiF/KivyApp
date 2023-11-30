from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import the Window class
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import the Window class

from .history_popup import * 
from .analaysis_popup import * 
from .recored_popup import *

class MainPageLayout(App):

    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions    

    def build(self):
        Window.size = (400, 300)
        layout = BoxLayout(orientation='vertical')
        self.recording_layout_button = Button(text="Start/Stop Recording")
        self.recording_layout_button.bind(on_release=lambda _:RecordPopup(self.definitions).build())  
        layout.add_widget(self.recording_layout_button)
        self.history_button = Button(text="History", font_size=20)
        self.history_button.bind(on_release=lambda _:HistoryPopup(self.definitions).build())  
        layout.add_widget(self.history_button)
        self.analysis_button = Button(text="Analysis", font_size=20)
        self.analysis_button.bind(on_release=lambda _:AnalysisPopup(self.definitions).build())  
        layout.add_widget(self.analysis_button)
        return layout




