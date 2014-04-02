#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Anton Lavrenov
# Copyright (c) 2014 Anton Lavrenov
#
# License: MIT
#

"""This module exports the Tslint plugin class."""

from SublimeLinter.lint import Linter, util


class Tslint(Linter):

    """Provides an interface to tslint."""

    syntax = 'typescript'
    cmd = ('tslint', '-f', '@')
    executable = None
    regex = (
        r'^.+?\[(?P<line>\d+), (?P<col>\d+)\]: '
        r'(?P<message>.+)'
    )
    error_stream = util.STREAM_BOTH
    config_file = ('-c', 'tslint')
