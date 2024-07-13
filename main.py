from ftplib import FTP
import os
import xml.etree.ElementTree as ET

FTP_SERVER = "localhost"
USERNAME = "nybsys"
PASSWORD = "12345"

TEMP_FOLDER = "temp"
LOCAL_FOLDER = "processed"
TRASH_FOLDER = "trash"


def download_file(filename) -> None:
    try:
        ftp = FTP(FTP_SERVER, USERNAME, PASSWORD)
        # print(ftp)
        os.makedirs(TEMP_FOLDER, exist_ok=True)
        with open(os.path.join(TEMP_FOLDER, filename), "wb") as file:
            ftp.retrbinary("RETR " + filename, file.write)
        print(f"Download: {filename}")

    except Exception as e:
        print(str(e))
        

download_file("A20240301.0010+0000-0015+0000_8C1F64.240B88008E2C.xml")

def move_file(source, destination):
    try:
        os.rename(source, destination)
        print(f"moved {os.path.basename(source)} to {destination}")
    except Exception as e:
        print(str(e))
        


# def download_new_files():
#     with FTP(FTP_SERVER) as ftp:
#         ftp.login(USERNAME, PASSWORD)
#         print(ftp.getwelcome())
#         # ftp.cwd("home/nybsys")
#         filenames = ftp.nlst()
#         # print(filenames)
#         for filename in filenames:
#             temp_file_path = os.path.join(TEMP_FOLDER, filename)
#             if not os.path.exists(temp_file_path):
#                 with open(temp_file_path, 'wb') as file:
#                     ftp.retrbinary(f"RETR {filename}", file.write)
#                 print(filename)
        
# download_new_files()