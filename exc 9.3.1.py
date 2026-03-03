# Write your python code here:
def my_mp3_playlist(file_path): 
#returns a tuple of (longest song, num of songs, most frequent author)
    authors = {}
    max_appearance, max_duration, num_songs = [0,0,0] 
    max_author, longest_song = [None, None]
    with open(file_path, "r") as f:
        cd_splitted_lines = f.readlines()
        for line in cd_splitted_lines:
            line_splitted = line.split(";")
            if len(line_splitted) < 2:
                continue #skips lines that don't have the right format
            num_songs += 1
            duration = convert_to_sec(line_splitted[2])
            if authors(line_splitted[1]) == None:
                authors[line_splitted[1]] = [(line_splitted[0],duration)]
            else:
                authors[line_splitted[1]].append((line_splitted[0],duration))
            appearance = len(authors[line_splitted[1]])

            if appearance > max_appearance:
                max_appearance = appearance
                max_author = line_splitted[1]
            if duration > max_duration:
                max_duration = duration
                longest_song = line_splitted[0]    
    return (longest_song, num_songs, max_author)
    

def convert_to_sec(duration): 
#converts a min:sec format to seconds
    times = duration.split(":")
    return 60*int(times[0])+int(times[1])
