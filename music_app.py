import json
import pyglet
import subprocess
from bs4 import BeautifulSoup
import requests


def download_mp4(url, to_name):
    subprocess.call(["F:/Anaconda3/Scripts/youtube-dl", "-o", str(to_name), str(url)])

def extract_sound(file, name):
    subprocess.call(["ffmpeg", "-i", file, "-vn", str(name) + ".ogg"])

def extract_sound_from_webm(file, name):
    subprocess.call(["ffmpeg", "-i", file, "-vn", "-ab", "128k", "-ar", "44100", "-y", str(name) + ".ogg"])

def search(song_name):
    res_page = requests.get('https://www.youtube.com/results?search_query=' + str(song_name).replace(" ", "+"))
    soup = BeautifulSoup(res_page.content, 'html.parser')
    return soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

def write_to_song_json_file(data):
    with open('song.json', 'w') as fp:
        json.dump(data, fp)

def show_songs():
    with open('song.json', 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        print(str(i + 1) + ". " + data[i]["Name"])


def main():
    while True:
        print("Pick an option:")
        print("1. Show all songs.")
        print("2. Show detail of a song.")
        print("3. Play a song.")
        print("4. Search and download songs.")
        print("5. Make a playlist.")
        print("6. Exit.")
        option = input()
        with open('song.json', 'r') as f:
            data = json.load(f)
        if int(option) == 1:
            if data == []:
                print("Song list is empty!")
            else:
                for i in range(len(data)):
                    print(str(i + 1) + ". " + data[i]["Name"])
        elif int(option) == 2:
            if data == []:
                print("Song list is empty!")
            else:
                print("Pick a song")
                for i in range(len(data)):
                    print(str(i + 1) + ". " + data[i]["Name"])
                song = int(input())
                print(data[song - 1]["Info"])
        elif int(option) == 3:
            print("Pick a song")
            for i in range(len(data)):
                print(str(i + 1) + ". " + data[i]["Name"])
            song = int(input())
            song_name = data[song - 1]["Name"] + ".ogg"
            player = pyglet.media.Player()
            player.queue(pyglet.media.load(song_name))
            player.play()
            exit = False
            while not exit:
                control = input()
                if control == "pause":
                    player.pause()
                if control == "play":
                    player.play()
                if control == "stop":
                    exit = True
            continue
        elif int(option) == 4:
            song_name = input("Enter the song you want to search.\n")
            video_list = search(song_name)
            song_list = []
            number_of_song = 0

            for video in video_list:
                 if song_name.lower() in str(video["title"]).lower() and number_of_song < 5:
                    song_list.append(video)
                    number_of_song += 1
            for i in range(len(song_list)):
                print(str(i + 1) + ". " + song_list[i]["title"])
            print("Enter the song whose position you want to download:")
            option_2 = input("Enter n if you don't want to download anything")
            if option_2 == "n":
                continue
            elif 1 <= int(option_2) <=5:
                download_mp4("https://youtube.com" + song_list[i - 1]['href'], song_name)
                extract_sound_from_webm(song_name + ".webm", song_name)
                extract_sound(song_name + ".mkv", song_name)
                extract_sound(song_name + ".mp4", song_name)
                with open('song.json', 'r') as f:
                    data = json.load(f)
                data.append({"Info":song_list[i].find_all("span")[0]["aria-label"], "Name": song_name})
                write_to_song_json_file(data)
            else:
                print('Plz')
                continue
        elif int(option) == 5:
            playlist = []
            player = pyglet.media.Player()
            while True:
                print("Pick a song")
                for i in range(len(data)):
                    print(str(i + 1) + ". " + data[i]["Name"])
                song = input("Press n if you want to stop\n")
                if song == "n":
                    break
                else:
                    song = int(song)

                song_name = data[song - 1]["Name"] + ".ogg"
                playlist.append(data[song - 1]["Name"])
                player.queue(pyglet.media.load(song_name))
            while True:
                print("Pick an option")
                print("1. Show playlist")
                print("2. Play the playlist")
                print("3. Exit")
                option_3 = input()
                if option_3 == "1":
                    for i in range(len(playlist)):
                        print(str(i + 1) + ". " + playlist[i])
                elif option_3 == "2":
                    player.play()
                    exit = False
                    while not exit:
                        print(playlist[0] + " is playing")
                        print("1. Play")
                        print("2. Next song")
                        print("3. Pause")
                        print("4. Exit")
                        option_4 = input()
                        if option_4 == "1":
                            player.play()
                        if option_4 == "2":
                            playlist.pop(0)
                            player.next_source()
                        if option_4 == "3":
                            player.pause()
                        if option_4 == "4":
                            exit = True
                elif option_3 == "3":
                    break

        elif int(option) == 6:
            break
        else:
            print("Please press a number from 1 to 5...")
            continue

main()