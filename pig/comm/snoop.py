import logging
import sys

from . import bus


def snoop(host='localhost'):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    socket = bus.connect_subscribe(host=host)

    while True:
        message = socket.recv_string()
        log.info(message)
