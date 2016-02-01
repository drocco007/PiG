# coding: utf-8

from . import bus


UDEV_EVENTS = u'®'


def udev_channel():
    socket = bus.subscribe(subscriptions=(UDEV_EVENTS,))

    while True:
        yield socket.recv_string()
