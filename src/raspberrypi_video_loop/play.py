from raspberrypi_video_loop.read_config import read_config
from raspberrypi_video_loop.read_directory import read_directory

from omxplayer import OMXPlayer
from time import sleep


def start():
    '''
        start the programm
        Returns:
    '''

    print("get video path from config")
    # load config
    video_path = read_config()

    # get mp4 files from video_path
    video_list = read_directory(video_path)

    if video_list:
        for video in video_list:
            print("Play: " + video)
            player = OMXPlayer(video)
            player.play()
            player.quit()
    else:
        print("There is no valid video in " + video_path)
        sleep(5)