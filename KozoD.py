from pytube import YouTube
from pytube import Playlist
from pytube import Search

import urllib.request
import re

import os
import time

def main():
    destination = "/home/balasundar/Downloads/"
    os.system("cls")
    print("\n\n")
    print("               ╔══════════════════════════════╗")
    print("               ║                              ║")
    print("               ║     X. Search on youtube     ║")
    print("               ║                              ║")
    print("               ║     1. Download Clip [LowQ]  ║")
    print("               ║                              ║")
    print("               ║     2. Download Audio        ║")
    print("               ║                              ║")
    print("               ║     3. Download Playlist     ║")
    print("               ║                              ║")
    print("               ╚══════════════════════════════╝\n")

    choix = input("votre choix : ")

    if choix == 'x':
        search()

    if choix == '1':
        clip_dl()

    if choix == '2':
        audio_dl()
    
    if choix =='3':
        playlist_dl()



def search():
    name = input('nom de la recherche : ').replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+name)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #print(video_ids)
    lien = "https://www.youtube.com/watch?v="+video_ids[0]
    video = YouTube(lien)

    print('\n | '"https://www.youtube.com/watch?v="+video_ids[0])
    print(' | chaine :', video.author,)
    print(' | vue :', video.views,)
    print(' | titre :', video.title,)
    print(' | size :', video.captions,)
    print("\n voulez vous télécharger la video ?\n 'oui' // 'non'")
    choix = input('\nVotre choix : ')

    if choix == 'oui':
        lien = "https://www.youtube.com/watch?v="+video_ids[0]
        video = YouTube(lien)
        streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        streams[0].download()
        print(' | size :', video.captions,)
        time.sleep(10)
        main()
    
    if choix == '/audio':
        lien = "https://www.youtube.com/watch?v="+video_ids[0]
        video = YouTube(lien)
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download()
        main()
    main()


def clip_dl():
    lien = input('Lien : ')
    try:
        video = YouTube(lien)
        print('[ CLEAN ]  [ 1/3 ]\n')
        os.system("cls")

        print('Get information / [ 2/3 ] \n')
        print(' | Chaine :', video.author,)
        print(' | Vue :', video.views,)
        print(' | Titre :', video.title,)
        print(' | Miniature :', video.thumbnail_url,)

        streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        #streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        # res='720p', fps='60fps',
        print(' [ CLEAN ]  [ 2/3 ]\n\n')
        print('Download in progress / [ 3/3 ]')
        
        streams[0].download()
        time.sleep(1)
        print('Download Completed!')
        main()

    except:
        print("Connection Error")
        time.sleep(1)
        main()





def audio_dl():
    lien = input('Lien : ')
    try:
        video = YouTube(lien)
        print('[ CLEAN ]  [ 1/3 ]\n')
        os.system("cls")

        print('Get information / [ 2/3 ] \n')
        print(' | chaine :', video.author, ' |')
        print(' | vue :', video.views, ' |')
        print(' | titre :', video.title, ' |')

        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        print(' [ CLEAN ]  [ 2/3 ]\n\n')

        print('Download in progress / [ 3/3 ]')
        audio.download()
        print('Download Completed!')
        main()

    except:
        print("Connection Error")
        main()


def playlist_dl():

    os.system("cls")
    print("\n\n")
    print("               ╔══════════════════════════════╗")
    print("               ║                              ║")
    print("               ║           Choice :           ║")
    print("               ║                              ║")
    print("               ║    1. Download Audio [SOON]  ║")
    print("               ║                              ║")
    print("               ║    2. Download Clip + Audio  ║")
    print("               ║                              ║")
    print("               ╚══════════════════════════════╝\n")

    pl_dl_choix = input("votre choix : ")

    if pl_dl_choix =='1':
        playlist_dl_audio()

    if pl_dl_choix =='2':
        playlist_dl_clip_audio()


def playlist_dl_audio():

    print('cette section sera bientot discponible')
    time.sleep(5)
    main()



def playlist_dl_clip_audio():

    lien = input('lien : ')
    p = Playlist(lien)
    print(p.title, 'contient', len(p), 'musiques ')
    
    print(f'Downloading: {p.title}')
    for video in p.videos:
        video.streams.first().download()
    time.sleep(5)
    main()



if __name__ == "__main__":
    main()