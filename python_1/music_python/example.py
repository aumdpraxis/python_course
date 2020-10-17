from note_manager import Note_Manager
import json

if __name__ == "__main__":
    with open('el_triste.json') as f:
        song = json.load(f)

    song_player = Note_Manager()
    song_player.init_stream()
    for compass in song:
    # compass= song[len(song)-1]
        for note in compass:
            song_player.run(note['n'],note['o'],note['t'])
    song_player.end_stream()
    