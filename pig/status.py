# coding=utf-8

# channel_handlers = {
#     u'®': device_status,
# }

from itertools import chain

from .camera import camera_connected
from .comm.bus import publish_all
from .comm.channels import udev_channel
from .lib.udev_monitor import is_camera_connected


def relay_status():
    initial_status = ['camera ready' if is_camera_connected()
                      else 'camera unavailable']
    camera_status = (connected and 'camera ready' or 'camera unavailable'
                     for connected in camera_connected(udev_channel()))

    publish_all(chain(initial_status, camera_status), channel=u'§')
