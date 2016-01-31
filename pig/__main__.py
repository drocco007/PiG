"""PiG: The Raspberry Pi Geotagger

Usage:
    pig [bus | snoop | pubtest | udev]
    pig show [camera | gps]
    pig (-h | --help)
    pig --version

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

from docopt import docopt

from .ui.commands import commands


arguments = docopt(__doc__, version='PiG 0.2')


# docopt command dispatcher. This is not my favorite, but... meh.
for subcommand in commands.keys():
    if arguments[subcommand]:
        commands[subcommand]()
        break
else:
    print arguments
