# flake8: noqa
from pkg_resources import DistributionNotFound, get_distribution

from sshspawner.spawner import SSHSpawner

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = '0.0.0'
