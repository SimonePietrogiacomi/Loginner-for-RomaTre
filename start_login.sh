#!/bin/bash

ssid="Rm3Wi-Fi"
# That's only for testing, it's the root of my home ssid :P
# ssid="Telecom"

path_to_this_file=$(readlink -f $0)
path_to_python_file=$(dirname $path_to_this_file)
python_file_name="login_romatre_selenium.py"
final_python_path="${path_to_python_file}/$python_file_name"

get_ssid () {
	network_name=`nmcli -t -f active,ssid dev wifi | egrep '^sì' | cut -d: -f2`
	if [[ "$network_name" == "" ]]
	then
		network_name=`nmcli -t -f active,ssid dev wifi | egrep '^yes' | cut -d: -f2`
	fi
}

get_connection () {
	get_ssid

	if [[ "$network_name" == "" ]]
	then
		result=1
	elif [[ "$network_name" =~ $ssid ]]
	then
		python3 "$final_python_path"
		result=$?
	else
		# You're in another network, you don't need me
		exit
	fi
}

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	get_connection
	if [[ "$result" == 1 ]]
	then
		sleep 2
	elif [[ "$result" == 2 ]]; then
	  notify-send "Username o password errati"
	  exit
	else
		notify-send "Connessione avvenuta!" "Puoi iniziare a navigare :)"
		exit
	fi
done
