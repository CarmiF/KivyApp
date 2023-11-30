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



class AnalysisPopup():

    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
        
    def build(self):
        layout = GridLayout(cols=7)
        
        # Dropdown for selecting months
        month_dropdown = DropDown()
        for month in calendar.month_name[1:]:
            btn = Button(text=month, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: month_dropdown.select(btn.text))
            month_dropdown.add_widget(btn)

        month_btn = Button(text='Select Month', size_hint=(None, None))
        month_btn.bind(on_release=month_dropdown.open)
        month_dropdown.bind(on_select=lambda instance, x: setattr(month_btn, 'text', x))
        layout.add_widget(month_btn)

        # Dropdown for selecting years
        year_dropdown = DropDown()
        for year in range(2000, 2030):
            btn = Button(text=str(year), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: year_dropdown.select(btn.text))
            year_dropdown.add_widget(btn)

        year_btn = Button(text='Select Year', size_hint=(None, None))
        year_btn.bind(on_release=year_dropdown.open)
        year_dropdown.bind(on_select=lambda instance, x: setattr(year_btn, 'text', x))
        layout.add_widget(year_btn)

        for key in calendar.day_abbr:
            layout.add_widget(Label(text=key))

        for i in range(1, 32):
            if i in calendar.monthrange(2023, 1):  # Update the year and month accordingly
                layout.add_widget(Label(text=str(i)))
            else:
                layout.add_widget(Button(text=str(i)))



        self.popup = Popup(title="Chocse the rec", content=layout, size_hint=(0.8, 0.7))
        self.popup.open()
        print("analysis")