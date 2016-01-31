# coding=utf-8

from time import sleep

from .bus import connect_publish


channels = u'a®¢§¶☭–—·×•¡±¿ß'


def check_one_two(host='localhost', port=5555, scheme='tcp'):
    socket = connect_publish(host=host, port=port, scheme=scheme)

    # Wait to give the connection time to settle
    sleep(0.5)

    socket.send('pubtest: check one, two, check check')

    for i in range(len(channels)):
        channel = channels[i % len(channels)]
        socket.send_string(u'{}: pubtest sample message'.format(channel))
        sleep(0.5)

    socket.send('pubtest: check done')
