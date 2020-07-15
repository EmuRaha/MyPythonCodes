#Dubstep
#song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND


def song_decoder(song):
    song=song.split("WUB")
    while '' in song:
        song.remove('')
    return " ".join(song)


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))











