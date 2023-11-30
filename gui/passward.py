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

from .main_page import MainPageLayout


# def check_password(password):
#     self = PasswordEntryApp()
#     self.password_correct=False
#     self.password=password
#     self.run()
#     return self.password_correct


class PasswordEntryApp(App):

    def __init__(self, definitions, **kwargs):
        super().__init__(**kwargs)
        self.definitions = definitions
        if self.definitions.open_password_page ==False:
            MainPageLayout(self.definitions).run()
            print("open_password_page == False")
            raise ValueError("open_password_page == False")

            

    
    def build(self):
        Window.size = (200, 150)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10,
            size_hint=(None, None),
            size=(300, 200))
        
        self.message_label = Label(
            text="Enter Your Password",
            font_size=20,
            size_hint=(1, 0.3),
            height=30
        )

        self.password_input = TextInput(
            password=True,
            font_size=20,
            size_hint=(1, 0.3),
            height=30,
            multiline=False,
            hint_text="Password"
        )

        self.submit_button = Button(
            text="Submit",
            size_hint=(1, 0.3),
            height=30)
        
        self.submit_button.bind(on_release=self.check_password)

        layout.add_widget(self.message_label)
        layout.add_widget(self.password_input)
        layout.add_widget(self.submit_button)

        return layout
    
    def check_password(self, entered_password):
        # Replace 'your_actual_password' with the correct password
        entered_password=self.password_input.text
        correct_password = self.definitions.password
        if entered_password == correct_password:
            self.password_input.text = ""  # Clear the input field
            self.message_label.text = "Password Correct!"
            self.password_correct=True
            print("before")
            self.stop()
            print("after")
            MainPageLayout(self.definitions).run()
             
             

        else:
            self.message_label.text = "Password Incorrect"
