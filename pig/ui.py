from gpiozero import LED
from signal import pause


def show_from_sequence(seq, pin=17):
    led = LED(pin)
    led.source = seq

    print
    print 'YES YOU NEED THIS PAUSE!'
    print

    pause()
