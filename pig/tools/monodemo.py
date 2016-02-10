# coding: utf-8

"""Monolithic demo program

Demonstration of the workflow and commands PiG uses to geotag an image.

"""

from collections import deque
from threading import Thread
from time import sleep, time

from gi.repository import GExiv2
from gps import gps, isotime, WATCH_ENABLE
from subprocess32 import Popen, PIPE, check_output


last_fix = deque([], 1)
running = True
geothread = None


def read_gps():
    global last_fix

    # p = Popen(
    #         'gpsbabel -T -i garmin -f usb: -o tabsep -F -'.split(' '),
    #         stdout=PIPE,
    #     )

    # try:
    #     while running:
    #         line = p.stdout.readline().split('\t')
    #         line = [line[7], line[8], line[18], line[20]]
    #         print line
    #         last_fix.append(line)
    # finally:
    #     print 'NOT QUITE DEAD YET!'
    #     p.kill()

    session = gps(mode=WATCH_ENABLE)

    while running:
        fix = session.next()

        if fix['class'] == 'TPV':
            fix = [fix.lon, fix.lat, fix.alt, isotime(fix.time)]
            # print fix
            last_fix.append(fix)


def init():
    global geothread

    geothread = Thread(target=read_gps)
    geothread.start()

    sleep(2)

    init_camera()


def init_camera():
    camera_time = check_output('gphoto2 --get-config /main/settings/datetime'.split(' '))
    systime = check_output(['date', '+%s'])

    print 'Camera time:', camera_time.strip()
    print 'Python: ', time()
    print 'System: ', systime.strip()
    print 'GPS:    ', last_fix[0][-1]


def capture():
    p = Popen(['gphoto2', '--wait-event-and-download'], stdout=PIPE)

    while True:
        line = p.stdout.readline()
        fix = last_fix[0]

        if not line.startswith('Saving'):
            continue

        image = line.rsplit(' ', 1)[-1].strip()

        geotag(image, fix)


def geotag(image, fix):
    fix = [float(item) for item in fix[:3]]
    print image, '←', fix
    exif = GExiv2.Metadata(image)
    exif.set_gps_info(*fix)
    exif.save_file()


def main():
    global running

    init()

    try:
        capture()
    except KeyboardInterrupt:
        pass

    running = False
    geothread.join()

    print last_fix
