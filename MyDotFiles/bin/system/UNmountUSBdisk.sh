#!/bin/zsh

notify-send "$(udisksctl unmount -b $(lsblk | grep "NAME\|sd[c-z]"|dmenu -l 10 |sed 's/\s.*$//'|sed 's/\W*/\/dev\//'))"
