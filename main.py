import yt_dlp
import glob
from pydub import AudioSegment
from pydub.utils import mediainfo
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download(link):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def main():
    global bitrate, tag, mixtape
    count = 0
    choice = input("Would you like to add a song to your mixtape? (y/n):")
    while choice == "y":
        link = input("Enter youtube link:")
        download(link)
        song_path = glob.glob("*.mp3")
        if "mixtape.mp3" in song_path:
            song_path.remove("mixtape.mp3")

        song = AudioSegment.from_mp3(song_path[0])
        if count == 0:
            mixtape = song
            count = count + 1
        else:
            mixtape = mixtape.append(song, crossfade=(10 * 1000))
            count = count + 1
        tag = mediainfo(song_path[0]).get('TAG', {})
        bitrate = mediainfo(song_path[0])["bit_rate"]
        os.remove(song_path[0])
        choice = input("Would you like to add another song? (y/n):")

    mixtape = mixtape.fade_out(2000)

    f = open("mixtape.mp3", 'wb')
    mixtape.export(f, format="mp3", tags=tag, bitrate=bitrate)
    print("Song exported as mixtape.mp3")
    f.close()



if __name__ == '__main__':
    main()


