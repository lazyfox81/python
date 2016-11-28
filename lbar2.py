#!/usr/bin/python
"""
Bar generator
"""
import sys
import os
import subprocess
import time
from collections import defaultdict
from threading import Thread

def start_bar(BG, FG):
    """
    Starts lemonbar and returns the handler
    """
    return subprocess.Popen(
        'lemonbar -B%s -F%s -a 30 -b -g x25 -f "Sans-9" -f "FontAwesome-9"' %
        (BG, FG),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

FG='#cccccc'
BG='#222222'
BG_ALT='#333333'
BAR_PROC = start_bar(BG, FG)

# Decorators
def schedule(time_in_seconds=None):
    def _scheduled(func):
        def _run():
            while True:
                try:
                    func()
                except:
                    traceback.print_exc(file=sys.stderr)
                time.sleep(time_in_seconds)

        if time_in_seconds is not None:
            Thread(target=_run).start()
        else:
            Thread(target=func).start()
        return func
    return _scheduled

@schedule(1)
def clock():
    global WIDGETS
    WIDGETS['clock'] = b'%%{A0:date_show:}%%{A:calendar:}%s%%{A}2%%{sA}' % time.strftime('%H:%M:%S').encode()

BAR_PROC.stdin.write(panel_str.encode('utf-8'))
BAR_PROC.stdin.flush()
