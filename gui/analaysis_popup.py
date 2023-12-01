from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import the Window class
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Import the Window class
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import calendar
import threading

from .utils.utils_main import *


class AnalysisPopup():

    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
        
    def build(self):
        
        main_layput = BoxLayout(orientation='vertical')
        
        select_month_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        self.month_dropdown = DropDown()
        for i in range(1, 13):
            btn = Button(text=str(i), size_hint_y=None, height=44)

            btn.bind(on_release=lambda btn: self.month_dropdown.select(btn.text))
            self.month_dropdown.add_widget(btn)

        self.month_btn = Button(text=str(get_current_month()), size_hint=(0.4, 1))
        self.month_btn.bind(on_release=self.month_dropdown.open)
        self.month_dropdown.bind(on_select=lambda instance, x: setattr(self.month_btn, 'text', x))

        select_month_layout.add_widget(self.month_btn)

        # Dropdown for selecting years
        self.year_dropdown = DropDown()
        for year in range(2000, 2030):
            btn = Button(text=str(year), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.year_dropdown.select(btn.text))
            self.year_dropdown.add_widget(btn)

        self.year_btn = Button(text=str(get_current_year()), size_hint=(0.4, 1))
        self.year_btn.bind(on_release=self.year_dropdown.open)
        self.year_dropdown.bind(on_select=lambda instance, x: setattr(self.year_btn, 'text', x))
        
        go_btn = Button(text = "Go", size_hint=(0.3, 1))
        go_btn.bind(on_release=lambda instance: self.create_calendar())

        select_month_layout.add_widget(self.year_btn)
        select_month_layout.add_widget(go_btn)

        # self.create_calendar()
        self.calendar_layout = GridLayout(cols=7, size_hint=(1, 0.8))


        main_layput.add_widget(select_month_layout)
        main_layput.add_widget(self.calendar_layout)


        self.popup = Popup(title="Chocse the rec", content=main_layput, size_hint=(None, None), size=(400, 300), auto_dismiss=True)
        self.popup.open()
        print("analysis")

    def create_calendar(self):
        
        self.calendar_layout.clear_widgets()  # Clear existing widgets

        calendar_layout = GridLayout(cols=7, size_hint=(1, 0.8))

        for key in calendar.day_abbr:
            calendar_layout.add_widget(Label(text=key))
        
        weekday, days_in_month = calendar.monthrange(int(self.year_btn.text), int(self.month_btn.text))

        for i in range(0, weekday):
            calendar_layout.add_widget(Label(text=""))
        
        self.data_folder_names = sort_folders_by_date(self.definitions.recorded_data_path)
        print(self.data_folder_names)

        for i in range(1, days_in_month + 1):
            # filter_date_strings(self.data_folder_names, i, )
            
            
            calendar_layout.add_widget(Button(text=str(i)))
        

        self.calendar_layout.add_widget(calendar_layout) 
        


        
        