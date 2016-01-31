"""PiG: The Raspberry Pi Geotagger

Usage:
    pig [bus | snoop | pubtest | udev]
    pig (-h | --help)
    pig --version

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

from docopt import docopt

arguments = docopt(__doc__, version='PiG 0.1')

from .commands import commands

for subcommand in commands.keys():
    if arguments[subcommand]:
        commands[subcommand]()
        break
else:
    print arguments
