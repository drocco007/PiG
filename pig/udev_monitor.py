import pyudev


camera_spec = {
    ('ID_VENDOR_FROM_DATABASE', 'Nikon Corp.'),
    ('ID_MODEL_FROM_DATABASE', 'D3000'),
}
camera = (camera_spec, 'Nikon D3000')

gps_spec = {
    ('ID_VENDOR_FROM_DATABASE', 'Garmin International'),
    ('ID_MODEL_FROM_DATABASE', 'GPS (various models)'),
}
gps = (gps_spec, 'Garmin etrex Venture')


def matches(device, spec):
    if not device.get('ID_BUS'):
        return False

    return spec & set(device.items()) == spec


def monitor():
    context = pyudev.Context()

    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('usb')

    for device in iter(monitor.poll, None):
        for spec, name in [camera, gps]:
            if matches(device, spec):
                yield ' '.join([device['ACTION'], name])
