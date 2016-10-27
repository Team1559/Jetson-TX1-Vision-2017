#!/usr/bin/python

import time


class Timer(object):

    def __init__(self):

        self.frames = 0
        self.isUpdate = True

        self.t_end = time.time() + 60


    def current_time(self):

        now = time.localtime(time.time())
        return now [5]


    def update(self):


