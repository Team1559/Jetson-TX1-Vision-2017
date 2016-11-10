#!/bin/bash

echo "now updating...";
echo "make sure to answer "yes" or "y" to any and all questions";
sudo chmod +x /home/ubuntu/Desktop/GoalFinder/contourfinder.py;
echo "...";
sudo cp aimbot.sh /etc/init.d;
echo "all done, to test:";
echo "1) restart with "sudo shutdown -r now";
echo "2) verify the camera is plugged in";
echo "3) type "top" and verify a "contourfinder.py" process is working";
echo "4) all done, if it's not running, you should probably tell somebody";
echo "if this failed, check to make the first line of "contourfinder.py" reads:";
echo "#!/usr/bin/python";
echo "if it was successful, congratulations, thanks for installing!";

