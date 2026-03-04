def my_mp3_playlist(file_path): 
    """
    Arguments: 
    file path
        the path refers to a file format: song_name;author;duration;
        where duration is in the format min:sec

    Returns:
        (longest song, num of songs, most frequent author)
    """
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
            continue #skips lines that don't have the right format
        song_name, author, length, _ = line.split(";")
        num_songs += 1
        duration = convert_to_sec(length)
        if authors.get(author) is None:
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
    
    
def convert_to_sec(duration): 
    """converts a min:sec format to seconds"""
    minutes, seconds = duration.split(":")
    return (60 * int(minutes)) + int(seconds)
 
