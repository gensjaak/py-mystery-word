#!/bin/bash

MIN_RANGE=1
MAX_RANGE=1000

tries=0
random=$(( RANDOM % MAX_RANGE + MIN_RANGE ))
userinput=""
username=""

echo $random

echo "--- 🔀 Jeu du mot mystère 🔀 ---"
echo
echo "Quel est tom nom ?"
read username

echo
echo "Saisis un nombre entre" $MIN_RANGE "et" $MAX_RANGE ": "
read userinput

while [ $userinput -ne $random ]
do
	((tries++))

	echo
	echo "Tutttttt"

	if [ $userinput -lt $random ]
	then
		echo "C'est beaucoup plus grand que ça ☝️ "
	else
		echo "Descends un tout petit peu 👇"
	fi

	echo
	echo "Ressayes, entre" $MIN_RANGE "et" $MAX_RANGE ": "
	read userinput
done

echo
echo
echo "Yesss 🏆"
echo "T'y es arrivé après "$tries" essais ⛹️‍♂️"
echo "Eh bah dis-donc" $username", tu es un sacré devin 👑"
echo
