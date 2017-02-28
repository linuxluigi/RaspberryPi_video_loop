import argparse
import raspberrypi_video_loop
from raspberrypi_video_loop import __version__

import datetime
import time


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('RaspberryPi_video_loop')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser


def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # start the program in an endless loop
    while True:
        ts = time.time()
        current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("Start new playlist @ " + current_time)


if __name__ == '__main__':
    main()
