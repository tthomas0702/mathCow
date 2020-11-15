#!/bin/bash

# by Lily and time 2020

# clear the screen
clear

figlet "* Cow-what *" 
sleep 5

# see who is playing and respond
echo "Hello, who am I talking to?"
read PLAYER_NAME
if [ "$PLAYER_NAME" == "Lily" ] ; then
    cowsay "You are Awsome Lily"
else
   cowsay "Your teeth are yucky!"
fi


# see what fovoorite color
echo "what is your favorite color?"
read COLOR
if [ "$COLOR" == "green" ]; then 
    cowsay "green is verry nice"
else
    # show small train
    sl -l
fi


# check if they want a fortune
echo "do you want your fortune?"
read ANSWER
if [ "$ANSWER" == "yes" ]; then 
    cowsay $(fortune -s)
else
    # show help me train
    sl -a
fi




