#!/bin/zsh

#KBD=$(cat /sys/class/leds/asus::kbd_backlight/brightness);
#KBD=$[KBD-1];
#if [ "$KBD" -lt "0" ];
#	then KBD=0;
#fi;
#echo $KBD;
#echo $KBD > /sys/class/leds/asus::kbd_backlight/brightness
ViewSonic="HDMI2 connected"

if xrandr | grep -q $ViewSonic;
	then echo "monitor found";
	xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0
else
	xrandr --auto
	echo "no match";
fi
