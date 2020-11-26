import requests
import os 
from tqdm import tqdm
from datetime import datetime


def download():
    now = datetime.now()
    download_dir = os.path.join(os.path.expanduser('~'),"Downloads")
    print("\n[*]DOWNLOAD PATH - ",download_dir,"\n")
    entered_link = input("Enter video link : ")

    video_link = "https://bx1.lithium.lk/presentation/%s/deskshare/deskshare.webm"%(entered_link.split("meetingId=")[1])
    audio_link = "https://bx1.lithium.lk/presentation/%s/video/webcams.webm"%(entered_link.split("meetingId=")[1])
    # print(video_link)
    video_down_path = os.path.join(download_dir,"nibm_v_3bmp4.mp4")
    audio_down_path = os.path.join(download_dir,"nibm_a_3bmp4.mp3")

    chunk_size = 1024

    vr= requests.get(video_link,stream=True)
    v_file_size = int(vr.headers['Content-length'])
    print("Video file downloading...")
    t = tqdm(total=v_file_size, unit='B', unit_scale=True, desc="nibm_v_3bmp4.mp4", ascii=True)
    with open(video_down_path,"wb") as f:
        for chunk in vr.iter_content(chunk_size=chunk_size):
            t.update(len(chunk))
            f.write(chunk)

    t.close()
    ar= requests.get(audio_link,stream=True)
    a_file_size = int(ar.headers['Content-length'])
    print("Audio file downloading...")
    t = tqdm(total=a_file_size, unit='B', unit_scale=True, desc="nibm_a_3bmp4.mp3", ascii=True)
    with open(audio_down_path,"wb") as f:
        for chunk in ar.iter_content(chunk_size=chunk_size):
            t.update(len(chunk))
            f.write(chunk)
    t.close()

def convert():
    now = datetime.now()
    download_dir = os.path.join(os.path.expanduser('~'),"Downloads")
    video_down_path = os.path.join(download_dir,"nibm_v_3bmp4.mp4")
    audio_down_path = os.path.join(download_dir,"nibm_a_3bmp4.mp3")

    name = input("\n\n   [#]Enter name to Session : ")

    os.system("ffmpeg.exe -i %s -i %s -c copy %s && del %s && del %s"%(
        video_down_path,
        audio_down_path,
        str(os.path.join(download_dir,name+".mp4")),
        video_down_path,
        audio_down_path))



def show_banner():
    print(
        '''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |   ______     | || | ____    ____ | || |   ______     | || |   _    _     | |
| |   / ____ `.  | || |  |_   _ \    | || ||_   \  /   _|| || |  |_   __ \   | || |  | |  | |    | |
| |   `'  __) |  | || |    | |_) |   | || |  |   \/   |  | || |    | |__) |  | || |  | |__| |_   | |
| |   _  |__ '.  | || |    |  __'.   | || |  | |\  /| |  | || |    |  ___/   | || |  |____   _|  | |
| |  | \____) |  | || |   _| |__) |  | || | _| |_\/_| |_ | || |   _| |_      | || |      _| |_   | |
| |   \______.'  | || |  |_______/   | || ||_____||_____|| || |  |_____|     | || |     |_____|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    V1.0

    BY SANDAKELUM PRIYAMANTHA 
    FOR NIBM VIDEO SESSION DOWNLOAD

        '''
    )

def menu():
    print('''
    **MENU**
    1. Download session
    0. exit 
    ''')
#show_banner()
while(True):
    show_banner()
    menu()
    opp = int(input("\nselect option -> "))
    if(opp == 1):
        download()
        convert()
    elif(opp == 0):
        print("bye")
        break
    else:
        print("Enter valide option")
