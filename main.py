from ftplib import FTP
import os, time


FTP_SERVER = "localhost"
USERNAME = "nybsys"
PASSWORD = "12345"

TEMP_FOLDER = "temp"
LOCAL_FOLDER = "processed"
TRASH_FOLDER = "trash"

if not os.path.exists(TEMP_FOLDER):
    os.makedirs(TEMP_FOLDER, exist_ok=True)
    
if not os.path.exists(LOCAL_FOLDER):
    os.makedirs(LOCAL_FOLDER, exist_ok=True)

def download_file() -> None:
    try:
        ftp = FTP(FTP_SERVER, USERNAME, PASSWORD)
        # print(ftp)
        # os.makedirs(TEMP_FOLDER, exist_ok=True)
        filenames = ftp.nlst()
        for filename in filenames:
            download_file_path = os.path.join(TEMP_FOLDER, filename)
            with open(download_file_path, "wb") as file:
                ftp.retrbinary("RETR " + filename, file.write)
            print(f"Download: {filename}")
            move_file(download_file_path, os.path.join(LOCAL_FOLDER, filename))
        ftp.quit()  # For temporary I quit this here

    except Exception as e:
        print(str(e))


def move_file(source, destination):
    try:
        os.rename(source, destination)
        print(f"Moved {os.path.basename(source)} to {destination}")
    except Exception as e:
        print(print(str(e)))

# as it will always monitor, here I define every 5sec it will run and check whether new file added or not.        
# while True:
download_file()
# time.sleep(5)
    
