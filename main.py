# This is a script used to search lyrics of songs for FCC banned words
# This is to help those creating playlists for radio shows and other media under FCC regulation

def open_file():
    lyrics = []
    f = open('Song.txt', 'r')
    for line in f:
        lyrics.append(line)

    return lyrics


def initialize_list():
    naughty_words = ['shit', 'piss', 'fuck', 'cunt', 'cocksucker', 'motherfucker', 'tits']
    return naughty_words


def search(list, lyrics):
    for line in lyrics:
        for word in list:
            if word in line:
                status = 'Explicit'
                print("Song is", status)
                exit(0)
            else:
                status = 'Good to Go'

    print("Song is", status)


if __name__ == "__main__":
    list = initialize_list()
    line = open_file()
    search(list, line)
