import os
import subprocess
from collections import OrderedDict


config_dir = os.path.expanduser('~/.pytmux/')


base_config = OrderedDict([
    ('name', 'example'),
    ('windows', [
        OrderedDict([
            ('name', 'editor'),
            ('command', 'emacs'),
        ]), {
            'name': 'default shell',
        }, {
            'command': 'redis-cli MONITOR',
        }, {}
    ])
])


def get_config_path(filename):
    return os.path.join(config_dir, '{}.json'.format(filename))


class Tmux(object):
    def __init__(self, session=None, directory=None):
        self.session = session
        self.directory = directory

    def call(self, *args, **kwargs):
        command = ('tmux',)
        return subprocess.call(command+args, **kwargs)

    def create(self):
        # Work around bug in tmux where it wont let you start another session
        # from inside of a session.
        env = os.environ.get('TMUX')
        if env:
            del os.environ['TMUX']

        self.call('new-session', '-s', self.session, '-d')

        if env:
            os.environ['TMUX'] = env

        if self.directory:
            self.set_option('default-path', self.directory)

    def send_keys(self, window, command):
        return self.call('send-keys',
                         '-t', '{}:{}.'.format(self.session, window),
                         command, '^M')

    def attach(self):
        if os.environ.get('TMUX'):
            self.call('switch', '-t', self.session)
        else:
            self.call('attach-session', '-t', self.session)

    def new_window(self, number, name, subdir=None):
        extra_args = ()
        if self.directory is not None:
            full_dir = os.path.join(self.directory, subdir) if subdir is not None else self.directory
            extra_args += ('-c', full_dir)
        if name:
            extra_args += ('-n', name)

        self.call('new-window', '-d', '-k',
                  '-t', '{}:{}'.format(self.session, number),
                  *extra_args)

    def set_option(self, option, value):
        self.call('set-option', '-q', '-t', self.session, option, value)
