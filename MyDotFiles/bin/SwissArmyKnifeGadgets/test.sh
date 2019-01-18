#! /bin/bash

file=~/Files/1-ToDo/to-do-list.md

#todoItem=$(sort -V $file | dmenu -l 10 | sed 's/^/+ /' | sed 's/+ +/-/' | tee -a $file)
todoItem=$(sort -V $file | dmenu -l 20 | sed 's/^/+ /' | tee -a $file)
sed -i '/^+ -.*/d' $file

if [ $(grep "^+ +" $file) ]
then
				echo najdu
else
				echo ninajdu
fi

#deleteItem=$(grep "+ +" $file | sed 's/+ +/+/')
#echo $deleteItem
#grep -v "^$deleteItem" $file > $file-tmp
#mv $file-tmp $file

sed -i 's/^+ +/-/' $file
grep "^+" $file | notify-send "ToDo list"
