import os
import subprocess
import re
from moviepy.editor import *
import time


def shell():
    os.system("clear")

    while True:
        print(
            """
    ·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
    ██▪ ██ ▪     ██· █▌▐█•█▌▐███•  ▪     ▐█ ▀█ ██▪ ██ ▐█ ▀█ •██  ▪     ▀▄ █·
    ▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
    ██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ ▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
    ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀        
    
                                                             
            """)
        time.sleep(3)
        print("1. mp4")
        print("2. mp3")
        print("3. Exit")

        try:
            inp = input()
            if int(inp) == 1:
                os.system("clear")
                print("[+] Incolla il link youtube di una playlist o di una canzone.")
                url = input("")
                time.sleep(3)
                os.system("mkdir mp4; cd mp4; youtube-dl -i -f mp4 --yes-playlist " + url)
                print("\n\n\n[+] Tutto fatto!")
                continue
            elif int(inp) == 2:
                os.system("clear")
                print("[+] Incolla il link youtube di una playlist o di una canzone.")
                url = input("")
                time.sleep(3)
                os.system("mkdir mp4; cd mp4; youtube-dl -i -f mp4 --yes-playlist " + url)
                print("[+] Tutto fatto, converto ora i file in mp3")
                foldermp3 = "./mp3/"
                foldermp4 = "./mp4/"
                os.system("mkdir mp3")

                for file in os.listdir(foldermp4):
                    mp4 = VideoFileClip(foldermp4 + file)
                    mp3 = mp4.audio
                    mp3.write_audiofile(foldermp3 + (file.split(".mp4")[0] + ".mp3"))
                    mp3.close()

                os.system("clear")
                print("\n\nVuoi eliminare i file mp4? ")

                if str(input("\n\n\n1. Si\n2. No\n")) == "1":
                    os.system("rm -r " + foldermp4)
                    os.system("clear")
                    print("[+] Tutto finito!")
                else:
                    os.system("clear")
                    print("[+] Tutto finito!")
            elif int(inp) == 3:
                os.system("clear")
                print("Auf wiedersehen!")
                exit()
            else:
                os.system("clear")
                print("Cio che hai digitato non è incluso nelle possibili scelte.")

        except Exception:
            os.system("clear")
            print("[-] Qualcosa è andato storto, riprova :(")
            continue


if __name__ == "__main__":
    shell()
