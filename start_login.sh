#!/bin/bash

ssid="Rm3Wi-Fi"

get_ssid () {
	network_name=`nmcli -t -f active,ssid dev wifi | egrep '^sì' | cut -d: -f2`
}

get_connection () {
	get_ssid

	if [[ "$network_name" == "" ]]
	then
		result=1
	elif [[ "$network_name" =~ "$ssid" ]]
	then
		python3 login_romatre_selenium.py
		result=$?
	fi
}

for i in 1 2 3 4 5
do
	get_connection
	if [[ "$result" == 1 ]]
	then
		sleep 2
	else
		notify-send "Connessione avvenuta!" "Puoi iniziare a navigare :)"
		exit
	fi
done
