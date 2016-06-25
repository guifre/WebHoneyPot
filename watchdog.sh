#!/bin/bash
installation='/opt/WebHoneyPot/'
script='webhoneypot.py'
if ps -ef | grep -v grep | grep -v watchdog | grep ${script} ; then
    exit 0
else
	cd ${installation}
	sudo python ${installation}/${script} &
fi
