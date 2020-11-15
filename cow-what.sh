#!/bin/bash

# by Lily and time 2020


clear

echo "Hello, who am I talking to?"

read PLAYER_NAME

if [ "$PLAYER_NAME" == "Lily" ] ; then
    cowsay "You are Awsome Lily"
else
   cowsay "Your teeth are yucky!"
fi

echo "what is your favorite color?"

read COLOR

if [ "$COLOR" == "green" ]; then 
    cowsay "green is verry nice"
else
    sl -l
fi


echo "do you want your fortune?"

read ANSWER

if [ "$ANSWER" == "yes" ]; then 
    cowsay $(fortune -s)
else
    sl -a
fi




