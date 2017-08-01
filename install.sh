#!/bin/sh

sudo clear # to immediately prompt sudo password, visual reasons
cd /tmp
git clone https://github.com/solinium/r-a-d.io-cli.git
sudo mkdir -p /etc/r-a-d.io-cli/
sudo cp /tmp/r-a-d.io-cli/cli.py /etc/r-a-d.io-cli/cli.py
sudo cp /etc/r-a-d.io-cli/audio.py /etc/r-a-d.io-cli/audio.py

pyver=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`

if [ $pyver -eq 0 ]; then
	sudo cp /tmp/r-a-d.io-cli/installfiles/p2 /usr/bin/radiocli
else 
	sudo cp /tmp/r-a-d.io-cli/installfiles/p3 /usr/bin/radiocli
fi

sudo chmod +x /usr/bin/radiocli
rm -rf /tmp/r-a-d.io-cli/
clear
echo 'Install Completed! Launch r/a/dio-cli with "radiocli".'