# coding: utf-8

def bus():
    from .comm.bus import message_bus
    message_bus()


def pubtest():
    from .comm.pubtest import check_one_two
    check_one_two()


def snoop():
    from .comm.snoop import snoop
    snoop()


def udev():
    from .comm.bus import publish_all
    from .comm.channels import UDEV_EVENTS
    from udev_monitor import monitor

    publish_all(monitor(), channel=UDEV_EVENTS)


commands = {
    'bus': bus,
    'pubtest': pubtest,
    'snoop': snoop,
    'udev': udev,
}
