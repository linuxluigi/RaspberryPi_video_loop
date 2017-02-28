import pytest
import raspberrypi_video_loop


def test_project_defines_author_and_version():
    assert hasattr(raspberrypi_video_loop, '__author__')
    assert hasattr(raspberrypi_video_loop, '__version__')
