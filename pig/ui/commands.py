# coding: utf-8


def bus():
    from ..comm.bus import message_bus
    message_bus()


def pubtest():
    from ..comm.pubtest import check_one_two
    check_one_two()


def snoop():
    from ..comm.snoop import snoop
    snoop()


def udev():
    from ..comm.bus import publish_all
    from ..comm.channels import UDEV_EVENTS
    from ..lib.udev_monitor import monitor

    publish_all(monitor(), channel=UDEV_EVENTS)


def show():
    from ..camera import camera_connected
    from ..ui.led import show_from_sequence
    from ..comm.channels import udev_channel

    show_from_sequence(camera_connected(udev_channel()), pin=17)


commands = {
    'bus': bus,
    'pubtest': pubtest,
    'snoop': snoop,
    'udev': udev,
    'show': show,
}
