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
    n = int(input("Enter number of songs you would like to add:"))
    for i in range(n):
        link = input(f"Enter link of song {i+1}:")
        download(link)

    song_paths = glob.glob("*.mp3")
    if "mixtape.mp3" in song_paths:
        song_paths.remove("mixtape.mp3")
    songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in song_paths]

    bitrate = mediainfo(song_paths[0])["bit_rate"]
    first_song = songs.pop(0)

    mixtape = first_song

    if len(songs) > 0:
        for song in songs:
            mixtape = mixtape.append(song, crossfade=(10 * 1000))

    mixtape = mixtape.fade_out(2000)

    f = open("mixtape.mp3", 'wb')
    mixtape.export(f, format="mp3", tags=mediainfo(song_paths[0]).get('TAG', {}), bitrate=bitrate)
    f.close()

    for i in song_paths:
        os.remove(i)




if __name__ == '__main__':
    main()


