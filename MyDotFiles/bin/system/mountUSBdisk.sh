#!/bin/zsh

#notify-send "$(udisksctl mount -b $(lsblk | grep "NAME\|sd[c-z]"|dmenu -l 10 |sed 's/\s.*$//'|sed 's/\W*/\/dev\//'))"
notify-send "UDISKSCTL :" "$($(lsblk | grep "sd[c-z][1-9]"|sed 's/^..s/s/' |dmenu -l 10 -p "(UN-)MOUNT USB" | awk '{if($7 == ""){print "udisksctl mount -b /dev/"$1}else{print "udisksctl unmount -b /dev/"$1}}'))"
