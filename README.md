# pigrrl2_shutdown_button
shutdown script for pigrrl 2     

place "pigrrl2_shutdown_button" directory in /home/pi on the pigrrl sd card
Move pishutdown.service to /etc/systemd/system/
Enable service 'sudo systemctl enable pishutdown.service'
Run service at boot 'sudo systemctl start pishutdown.service'
