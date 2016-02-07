# coding: utf-8

import zmq


_context = None


def get_context():
    global _context

    if not _context:
        _context = zmq.Context()

    return _context


def get_socket(socket_type):
    return get_context().socket(socket_type)


def publish(host='localhost', port=5555, scheme='tcp'):
    socket = get_socket(zmq.PUB)
    socket.connect('{}://{}:{}'.format(scheme, host, port))
    return socket


def subscribe(host='localhost', subscriptions=(u'',), port=5556,
              scheme='tcp'):
    socket = get_socket(zmq.SUB)
    socket.connect('{}://{}:{}'.format(scheme, host, port))

    for subscription in subscriptions:
        socket.setsockopt_string(zmq.SUBSCRIBE, subscription)

    return socket


def message_bus(pub_port=5556, sub_port=5555):
    bus_in = get_socket(zmq.XSUB)
    bus_out = get_socket(zmq.XPUB)

    bus_in.bind('tcp://*:{port}'.format(port=sub_port))
    bus_out.bind('tcp://*:{port}'.format(port=pub_port))

    print '∅MQ multi-publisher message bus {sub_port}→ {pub_port}' \
        .format(sub_port=sub_port, pub_port=pub_port)

    zmq.device(zmq.FORWARDER, bus_in, bus_out)

    # shouldn't get here
    bus_in.close()
    bus_out.close()


def init_message_bus(pub_port=5556, sub_port=5555):
    from ..lib.process_utils import spawn_daemon_process

    return [spawn_daemon_process(message_bus, call_kw={'pub_port': pub_port,
                                                       'sub_port': sub_port})]


def publish_all(seq, channel='', host='localhost', port=5555, scheme='tcp'):
    socket = publish(host=host, port=port, scheme=scheme)

    from time import sleep
    sleep(0.1)

    for message in seq:
        socket.send_string(u''.join([channel, message]))
