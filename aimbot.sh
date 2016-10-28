#!/bin/bash

### BEGIN INIT INFO

# Provides:	        aimbot.sh

# Required-Start:	mountall

# Required-Stop:	$remote_fs $syslog

# Default-Start:	2 3 4 5

# Default-Stop:		0 1 6

# Short-Description:    start at boot

# Description:		provided by daemon

### END INIT INFO

/home/ubuntu/Desktop/GoalFinder/contourfinder.py 2>/home/ubuntu/Desktop/GoalFinder/aimbotlog
