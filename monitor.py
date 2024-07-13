import xml.etree.ElementTree as ET
import os, time
# from main import move_file

TEMP_FOLDER = "temp"
LOCAL_FOLDER = "processed"
TRASH_FOLDER = "trash"


if not os.path.exists(TRASH_FOLDER):
    os.makedirs(TRASH_FOLDER, exist_ok=True)
    
        
def process_xml(filename):
    data_dict = {}
    filepath = os.path.join(LOCAL_FOLDER, filename)
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        for element in root.findall("*"):
            data_dict[element.tag] = element.text
        print(f"Processed file: {filename}")
        print(data_dict)
        
    except Exception as e:
        print(str(e))
        
        
def monitor_folder(folder):
    while True:
        for filename in os.listdir(folder):
            if filename not in os.listdir(folder):
                continue
            source = os.path.join(folder, filename)
            process_xml(filename)
            move_file(source, os.path.join(TRASH_FOLDER, filename))
        time.sleep(5)



def move_file(source, destination):
    try:
        os.rename(source, destination)
        print(f"Moved {os.path.basename(source)} to {destination}")
    except Exception as e:
        print(print(str(e)))


        
monitor_folder(LOCAL_FOLDER)