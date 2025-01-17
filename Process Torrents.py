import os
import zipfile
import subprocess
import sys
import time

#========== Settings ============

min_file_size = 1                                           # File should be at least X Gb to extract it from the zip
source_path = "N:Torrents"                                  # Source media archive folder
temp_path = "N:Torrents/-=Decompressed=-"                   # Holding folder for un-zipped files waiting to be renamed
format_info = "{drive}/{plex}"                              # Normal filebot format for renaming and final location of renamed media
action = "move"                                             # Normal filebot action aka: move | copy | symlink | hardlink
movie_db = "TheMovieDB"                                     # Normal filebot db value aka: TheMovieDB | OMDb
tv_db ="TheMovieDB::TV"                                     # Normal filebot db value aka: TheMovieDB | OMDb

#========== Settings ============


def extract_large_files(zip_folder, extract_folder):
    for root, _, files in os.walk(zip_folder):
        for file in files:
            if file.endswith('.zip'):
                print(".zip found, extracting....                      ", end="\r")
                zip_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    large_files = [zi for zi in zip_ref.infolist() if zi.file_size > min_file_size * 1024 * 1024 * 1024]
                    for zip_info in large_files:
                        zip_info.filename = os.path.basename(zip_info.filename)
                        zip_ref.extract(zip_info, extract_folder)
                os.remove(zip_path)
                process_movies_with_filebot(temp_path)
    bar = [
        "Waiting for .zip [=     ]",
        "Waiting for .zip [ =    ]",
        "Waiting for .zip [  =   ]",
        "Waiting for .zip [   =  ]",
        "Waiting for .zip [    = ]",
        "Waiting for .zip [     =]",
        "Waiting for .zip [    = ]",
        "Waiting for .zip [   =  ]",
        "Waiting for .zip [  =   ]",
        "Waiting for .zip [ =    ]",
    ]
    i = 0
    print("                                                            ", end="\r")
    
    while True:
        print(bar[i % len(bar)], end="\r")
        i += 1
        zip_files = [f for f in os.listdir(zip_folder) if f.endswith('.zip')]
        if zip_files:
            extract_large_files(zip_folder, extract_folder)
        else:
            time.sleep(1)

def process_movies_with_filebot(temp_path):
    # PROCESS MOVIES FIRST
    if not os.path.exists(temp_path):
        print(f"The folder {temp_path} does not exist.")
        return

    command = [
        'filebot', '-rename', '-non-strict', temp_path,
        '--db', movie_db,
        '--format', format_info,
        '--action', action
    ]

    try:
        print("Processing MOVIES with FileBot...                ")
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FileBot processing MOVIES completed successfully.")
        try:
            print(result.stdout.decode())
        except:
            print(result.stdout)
            
    except subprocess.CalledProcessError as error:
        print("An error occurred while processing MOVIES with FileBot or there was nothing found by FileBot for MOVIES.")
        try:
            print(error.stderr.decode())
        except:
            print(error.stderr)
    process_tvshows_with_filebot(temp_path)

def process_tvshows_with_filebot(temp_path):
    # PROCESS TV SHOWS NEXT
    if not os.path.exists(temp_path):
        print(f"The folder {temp_path} does not exist.")
        return

    command = [
        'filebot', '-rename', '-non-strict', temp_path,
        '--db', tv_db,
        '--format', format_info,
        '--action', action
    ]

    try:
        print("Processing TV SHOWS with FileBot...                ")
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FileBot processing TV SHOWS completed successfully.")
        try:
            print(result.stdout.decode())
        except:
            print(result.stdout)
            
    except subprocess.CalledProcessError as error:
        print("An error occurred while processing TV SHOWS with FileBot or there was nothing found by FileBot for TV SHOWS.")
        try:
            print(error.stderr.decode())
        except:
            print(error.stderr)
    time.sleep(5)
    main()
    
def main():
    
    extract_large_files(source_path, temp_path)


if __name__ == "__main__":
    main()
