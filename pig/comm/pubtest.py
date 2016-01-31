from time import sleep

from .bus import connect_publish


def check_one_two(host='localhost', port=5555, scheme='tcp'):
    socket = connect_publish(host=host, port=port, scheme=scheme)

    # Wait to give the connection time to settle
    sleep(0.5)

    socket.send('pubtest: check one, two, check check')

    for i in range(10):
        socket.send('{}: pubtest sample message'.format(i))
        sleep(0.5)

    socket.send('pubtest: check done')
