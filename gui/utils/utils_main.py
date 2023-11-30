
import datetime
import os

def get_time_and_date():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    return formatted_datetime

def sort_folders_by_date(folder_path):
    folders = [
        f for f in os.listdir(folder_path) 
               if os.path.isdir(os.path.join(folder_path, f))]
    sorted_folders = sorted(folders, key=lambda x: extract_date_from_folder_name(x))
    return sorted_folders

def extract_date_from_folder_name(folder_name):
    try:
        # Split the folder name by the first underscore and then by the hyphen to extract the date part
        date_str = folder_name.split('_', 1)[0].split('-', 1)[0]
        # Attempt to convert the date string into a tuple of integers
        date_parts = tuple(map(int, date_str.split('-')))
        return date_parts
    except (ValueError, IndexError):
        # If there's an issue with the expected format, return a date far in the past (it will be placed at the start)
        return (0, 0, 0)

def get_new_subfolder_path(recorded_data_path):
    formatted_datetime= get_time_and_date()
    new_dirctory_path= os.path.join(recorded_data_path, formatted_datetime)
    if not os.path.exists(new_dirctory_path):
        os.makedirs(new_dirctory_path)
    newSubTextPath= new_dirctory_path + "\\text.txt"
    newSubAudioPath = new_dirctory_path + "\\audio.wav"
    return newSubAudioPath, newSubTextPath

# def set_recorded_data_path():
#     current_directory = os.getcwd()
#     recordedDataPath=current_directory+"\\"+ RECORDED_DATA_DIRECTORY_NAME
#     return recordedDataPath

# def get_recorded_data_path():
#     current_directory = os.getcwd()
#     recordedDataPath=current_directory+"\\"+ RECORDED_DATA_DIRECTORY_NAME
#     return recordedDataPath
