import os


def read_directory(video_path):
    '''
            read the video_path for any mp4 files
            Returns: a list of mp4 files
    '''

    video_list = []

    for file in os.listdir(video_path):
        if file.endswith(".mp4"):
            video_list.append(video_path + file)

    return video_list
