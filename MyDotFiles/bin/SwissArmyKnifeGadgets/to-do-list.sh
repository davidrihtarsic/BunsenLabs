#! /bin/bash

file=~/Files/1-ToDo/to-do-list.md
cat $file > $file-temp
selectedItem=$(sort -V $file | dmenu -l 20 -p "ToDo:")
echo $selectedItem

if [[ $selectedItem =~ ^\+.*$  ]]
then
				grep -v "$selectedItem" $file>$file-temp &&
				doneItem=$(echo $selectedItem | sed 's/^\+/\-/') &&
				echo $doneItem >> $file-temp &&
				notify-send "narejeno" "$selectedItem"
elif [[ $selectedItem =~ ^\-.*$  ]]
then
				deleteItem=$(echo $selectedItem | sed 's/^\-//') &&
				grep -v "$deleteItem" $file>$file-temp &&
				notify-send "izbrisano" "$deleteItem"
elif [[ $selectedItem =~ ^$  ]]
then
				echo exit
else
				echo dodajam
				echo "+ $selectedItem" >> $file-temp &&
				notify-send "dodano" "$selectedItem"
fi

sort -V $file-temp > $file
rm $file-temp
			

