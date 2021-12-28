import os
import fnmatch

import id3reader_p3
import id3reader_p3 as id3reader

# def search_files(root, extension):
#     name = '.{}'.format(extension)
#     length = len(name)
#     for path, directory, file in os.walk(root):
#         for f in file:
#             if f[-length:] == name:
#                 yield os.path.join(path, f)


def search_files(root, extension):
    for path, directories, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)  # use it in yielded values

file_path = "music"
# file_path = "E:\\Users\\Raju Jogani\\Downloads"
# C:\\Users\\Raju Jogani\\IdeaProjects
files_list = search_files(file_path, 'emp3')

error_list = []

for f in files_list:
    try:
        id3r = id3reader_p3.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title'),
        ))
    except:
        error_list.append(f)

for item in error_list:
    print(item)
