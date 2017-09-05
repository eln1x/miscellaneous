if [ "$(id -u)" != "0" ];then
	echo "Run it as root"
	exit
fi
if [ ! -d ~/backup ];then
	mkdir ~/backup
fi
networksetup -setairportpower airport off
mv /Library/Preferences/SystemConfiguration/com.apple.airporti.preferences.plist ~/backup/com.apple.airport.preferences.plist
mv /Library/Preferences/SystemConfiguration/com.apple.network.identification.plist ~/backup/com.apple.network.identification.plist
mv /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist ~/backup/NetworkInterfaces.plist
mv /Library/Preferences/SystemConfiguration/preferences.plist ~/backup/preferences.plist
reboot



