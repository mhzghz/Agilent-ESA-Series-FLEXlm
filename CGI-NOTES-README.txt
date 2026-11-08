To setup Wine to be called from a Perl CGI:

sudo mkdir -p /var/www/.wine
sudo chown -R www-data:www-data /var/www/.wine
sudo -u www-data WINEPREFIX=/var/www/.wine wineboot --init
sudo apt-get install xvfb
sudo systemctl edit apache2

Add the following lines to turn off the syscall filtering and memory protection:

[Service]
SystemCallFilter=
SystemCallArchitectures=
MemoryDenyWriteExecute=no

sudo systemctl daemon-reload
sudo systemctl restart apache2   
