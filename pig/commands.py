def bus():
    from .comm.bus import message_bus
    message_bus()


def pubtest():
    from .comm.pubtest import check_one_two
    check_one_two()


def snoop():
    from .comm.snoop import snoop
    snoop()


commands = {
    'bus': bus,
    'pubtest': pubtest,
    'snoop': snoop,
}
