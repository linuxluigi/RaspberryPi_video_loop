import ConfigParser, os


def read_config():
    '''
    Read the config '/etc/RaspberryPi_video_loop.conf' and return it's content
    Returns:
        String Video Path
    '''

    config_path = "/etc/RaspberryPi_video_loop.conf"

    # read config
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_path))

    return config.get('Dir', 'dir', 0)
