#!/bin/zsh

#KBD=$(cat /sys/class/leds/asus::kbd_backlight/brightness);
#KBD=$[KBD-1];
#if [ "$KBD" -lt "0" ];
#	then KBD=0;
#fi;
#echo $KBD;
#echo $KBD > /sys/class/leds/asus::kbd_backlight/brightness
ViewSonic="HDMI-2 connected"

if xrandr | grep -q $ViewSonic;
	then echo "monitor found";
	xrandr --output HDMI-2 --mode 1920x1080 --pos 1920x0
else
	echo "no match";
fi