"""returns a tuple of (longest song, num of songs, most frequent author)"""
def my_mp3_playlist(file_path): 
    authors = {}
    max_appearance = 0
    max_duration = 0 
    num_songs = 0 
    max_author  = None
    longest_song = None
    with open(file_path, "r") as f:
        song_entries = f.readlines()
    for line in song_entries:
        if line.count(";") != 3:
            continue #skips lines that don't have the right folrmat
        song_name, author, length, _ = line.split(";")
        num_songs += 1
        duration = convert_to_sec(length)
        if authors.get(author) == None:
            authors[author] = [(song_name,duration)]
        else:
            authors[author].append((song_name,duration))
        appearance = len(authors[author])

        if appearance > max_appearance:
            max_appearance = appearance
            max_author = author
        if duration > max_duration:
            max_duration = duration
            longest_song = song_name    
    return (longest_song, num_songs, max_author)
    
    """converts a min:sec format to seconds"""
def convert_to_sec(duration): 
    minutes, seconds = duration.split(":")
    return (60 * int(minutes)) + int(seconds)
 
