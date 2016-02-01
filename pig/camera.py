def camera_connected(messages):
    for message in messages:
        if u'Nikon D3000' in message:
            yield u'add' == message[1:4]
