from .comm.bus import subscribe
from .comm.channels import UDEV_EVENTS


def camera_connected():
    socket = subscribe(subscriptions=(UDEV_EVENTS,))

    while True:
        message = socket.recv_string()

        if 'Nikon D3000' in message:
            yield 'add' == message[1:4]
