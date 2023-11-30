

from gui.passward import PasswordEntryApp
import os

def set_recorded_data_path(recorded_data_directory):
    current_directory = os.getcwd()
    recorded_data_path = os.path.join(current_directory, recorded_data_directory)
    return recorded_data_path

PASSWORD = "123"
ENCRYPTION = FalseTRANSCRIBE = True
RECORDED = True
RECORDED_DATA_PATH = "C:\Repos\diaryProject\kivy_and_pc\RecordedData"
TRANSCRIBE=True

class Definitions():
    def __init__(self):
        self.password="123"
        self.encryption  = True
        self.recored = True
        self.password= PASSWORD
        self.transcribe = True
        self.recorded_data_directory = "RecordedData"
        self.recorded_data_path = set_recorded_data_path(self.recorded_data_directory)
        self.open_password_page = False
        self.key = b'your_secret_key123'

        print(self.recorded_data_path)



if __name__ == '__main__':
    
    definitions = Definitions()
    PasswordEntryApp(definitions).run()

    