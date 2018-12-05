#!/bin/bash
cvt 1280 1024 60 &&
sudo xrandr --newmode "1280x1024"  109.00  1280 1368 1496 1712  1024 1027   1034   1063 -hsync +vsync &&
sudo xrandr --addmode VGA1 1280x1024 &&
arandr