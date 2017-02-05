sudo su
cd /opt
git clone https://github.com/guifre/WebHoneyPot.git
touch /var/log/webhoneypot.log
chown -R pi:pi WebHoneyPot/
chown pi:pi /var/log/webhoneypot.log
exit
cd WebHoneyPot
setsid python 