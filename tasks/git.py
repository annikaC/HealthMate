"""Helpers for git."""
import subprocess


def config_get(name):
    """Get Git config."""
    output = subprocess.check_output(['git', 'config', '--get', name])
    return output.splitlines()[0]  # Chomp the trailing newline


def email():
    """Get git user email."""
    return config_get('user.email')


def name():
    """Get git username."""
    return config_get('user.name')
