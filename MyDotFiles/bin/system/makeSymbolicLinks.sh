#!/bin/zsh

OIFS="$IFS"
IFS=$'\n'
SOURCE=~/Files/GitHub_noSync/BunsenLabs/MyDotFiles
SOURCE_LEN=${#SOURCE}

DESTINATION=~

for file in $(find $SOURCE -type f)
do
	SOURCE_FILE_NAME=${file:t}
	SOURCE_FILE_PATH=${file:h}
	SOURCE_DIR_STRUC=${SOURCE_FILE_PATH: $SOURCE_LEN}
	
	DEST_LINK_PATH=$DESTINATION$SOURCE_DIR_STRUC
	DEST_LINK_NAME=$SOURCE_FILE_NAME
	LINK="$DEST_LINK_PATH/$DEST_LINK_NAME"

	#test
	echo "---------"
	echo "Source file:$file"
	echo "Source file path: $SOURCE_FILE_PATH"
	echo "Source file name: $SOURCE_FILE_NAME"
	echo "Source dir. structure: $SOURCE_DIR_STRUC"
	echo "Link path: $DEST_LINK_PATH"
	echo "Link name: $DEST_LINK_NAME"


	if [[ -a $LINK ]]; then
		echo "File exist!"
		if [[ -f $LINK ]]; then
			echo "File is 'regular file'"
			if [[ -h $LINK ]]; then
				echo "File is a 'symbolic link'"
				echo "deleting link..."
				rm -v $LINK
			else
				echo "Renameing file... to $LINK.bck"
				mv -v $LINK $LINK.bck
			fi
		fi
	fi
	mkdir -p -v $DEST_LINK_PATH
	ln -s -v $file "$DEST_LINK_PATH/$DEST_LINK_NAME"
done
IFS="$OIFS"
