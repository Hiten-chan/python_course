# -*- coding: utf-8 -*-
from random import shuffle
import re


class Song:
    def __init__(self, name, artist, album, position, year, time):
        self.name = name
        self.artist = artist
        self.album = album
        self.position = str(position)
        self.year = str(year)
        self.time = str(time)

    def __repr__(self):
        song = "%s\t%s\t%s\t%s\t%s\t%s" % (self.name, self.artist, self.album, self.position, self.year, self.time)
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False

songs = []


def import_song(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    lines = f.read().split('\n')
    for l in lines:
        songs.append(Song(*l.split('\t')))
    f.close()
    return songs


def export_songs(songs, file_names):
    file = open(file_names, 'w', encoding='utf-8')
    file.write('\n'.join(str(s) for s in songs))
    file.close()


def shuffle_songs(songs):
    shuffle(songs)
    return songs


# Вывести самого часто встречающегося исполнителя (по числу песен)
def popular_artist(songs):
    artists = []
    d = {}
    m, index = 0, 0

    for song in songs:
        song_artist = song.artist
        artists.append(song_artist)
    for a in artists:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
        if d[a] > m:
            m, index = d[a], a
    print(index)


# Вывести самую длинную песню
def long_song(songs):
    max_dur = 0
    name_artist = str()
    for song in songs:
        if int(song.time) > max_dur:
            max_dur = int(song.time)
            name_artist = '%s\t%s' % (song.name, song.artist)
    print(name_artist)


# Вывести на экран самый длинный (по длительности) альбом
def long_album(songs):
    d = {}
    for song in songs:
        name_album = '%s\t%s' % (song.album, song.artist)
        song_time = int(song.time)
        if name_album in d:
            d[name_album] += song_time
        else:
            d[name_album] = song_time
    for key, value in d.items():
        if value == max(d.values()):
            print(key)


# Вывести 10 слов наиболее часто встречающихся в названиях песен
def popular_word(songs):
    words = []
    d = {}
    for song in songs:
        words.append(re.findall('[a-z]+', song.name.lower()))
    for song in words:
        for word in song:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    l = []
    i = 0
    out = []
    for key, value in d.items():
        l.append([value, key])
    words_sorted = sorted(l, reverse=True)
    if len(words_sorted) > 10:
        while i < 10:
            for k in range(0, 10):
                j = words_sorted[i]
                out.append(j[1])
                i += 1
                break
    else:
        for j in words_sorted:
            out.append(j[1])
    print("\t".join(out))


def hunky_artist(songs):
    d_main = {}
    d2 = {}
    m, index = 0, 0
    for song in songs:
        artist_album = '%s\t%s' % (song.artist, song.album)
        if artist_album not in d2:
            try:
                d2[artist_album] = 1
                d_main[song.artist] += 1
            except KeyError:
                d_main[song.artist] = 1
        if d_main[song.artist] > m:
            m, index = d_main[song.artist], song.artist
    print(index)

#import_song("songs1.txt")
#export_songs(songs, 'out.txt')

#popular_artist(songs)
#long_song(songs)
#long_album(songs)
#popular_word(songs)
#hunky_artist(songs)
