# nybsys_ftp


<h3>Task Requirements: </h3>

1. Basic Setup:
- Run the FTP server container using the docker-compose given below
- Put the sample xml files linked below into the FTP server

2. Download and Store Files:
- Keep Downloading newly uploaded xml files from the FTP server and keeps
them in a TEMP folder while download is finished.
- When download is complete move the file to a Local folder
3. Monitor Designated Local Folder:
- Continuously monitor the designated local folder for any new files being
moved into it. This folder is different from the temporary folder used above

4. Processing Files:
- Once a new xml file is detected in the local folder, process it and extract out
all the values and the parameter names from it.
- Process the xml file and convert the data into a python dictionary. Parameter
names as key and values as values of the dictionary.
- Print the dictionary
5. Move Files:
- After processing, move the files to a trash folder for later observation.

## 1. Create virtual environment by
    python -m venv tenv

## 2. Activate the 'tenv' in WindowsOS
    tenv\Scripts\activate

## or in MacOS
    source tenv/bin/activate

As it is required to run Docker file by command <b>"docker-compose up -d"</b>

I've attached two screenshots of the output.

<b>download from FTP </b>

![download from FTP](/download_from_ftp.png)

<b>process XML and moved to trash </b>

![process XML and moved to trash](/monitor_and_trash.png)