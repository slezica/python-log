import logging, sys, blessings
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

colors = True
format = '{levelname: <8} {msg}'

term = blessings.Terminal()

logging.basicConfig()


class Logger(logging.Logger):
    def __init__(self, name, level = DEBUG):
        super(Logger, self).__init__(name, level)

        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(self)
        self.addHandler(console)

    def format(self, record):
        color = {
            'DEBUG'   : term.bold_blue,
            'INFO'    : term.bold_white,
            'WARNING' : term.bold_yellow,
            'ERROR'   : term.bold_red,
            'CRITICAL': term.bold_white_on_red
        }[record.levelname] if colors else lambda string: string

        string = format.format(**record.__dict__)
        return color(string)

    # def color_format(self, record)


default = Logger('default', DEBUG)


def message(level, *objects):
    method = getattr(default, level)
    string = ' '.join(map(str, objects))

    method(string)
    return objects[0]

def d(*objects): return message('debug'   , *objects)
def i(*objects): return message('info'    , *objects)
def w(*objects): return message('warning' , *objects)
def e(*objects): return message('error'   , *objects)
def c(*objects): return message('critical', *objects)