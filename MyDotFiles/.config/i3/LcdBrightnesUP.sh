#!/bin/zsh

LED=$(cat /sys/class/backlight/intel_backlight/brightness);
LED=$[LED*2];

if [ "$LED" -lt "10" ];
	then LED=12;
fi;

if [ "$LED" -gt "1500" ];
	then LED=1500;
fi;
echo $LED;
echo $LED > /sys/class/backlight/intel_backlight/brightness