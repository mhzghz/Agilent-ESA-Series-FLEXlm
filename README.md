# Agilent-ESA-Series-FLEXlm
Agilent ESA-Series Spectrum Analyzer and ESG-Series Signal Generator FLEXlm Crypt Generator

Experimental interactive CGI to generate license keys for enabling options on older Agilent ESA-series spectrum analyzers and ESG-series RF signal generators.

Some options may require additional hardware or updated firmware.

Requires your web server to have CGI enabled. For Apache:
     
     $ sudo a2enmod cgi
     Enabling module cgi.
     To activate the new configuration, you need to run:
      (sudo) systemctl restart apache2

Requires a writable 'tmp' directory within your 'cgi-bin' directory and the ability for your HTTP server to work on files from that 'cgi-bin/tmp' directory:
     
     $ mkdir /www/cgi-bin/tmp
     $ chmod 777 /www/cgi-bin/tmp
      
Requires the installation of Wine: https://www.winehq.org

To call Wine from a Perl CGI, you may need to turn off the syscall filtering and memory protection.

You can do that via: `sudo systemctl edit apache2`

And adding the following:

```
[Service]
SystemCallFilter=
SystemCallArchitectures=
MemoryDenyWriteExecute=no
```
Save and then run: `sudo systemctl daemon-reload` and `sudo systemctl restart apache2`

Be sure to check the `CGI-NOTES-README.txt` file for more information on setting up Wine/Apache user environment.

It also requires the installation of the included 'lmcryptTMOMID01.exe' binary into '/usr/local/bin'.



***Try it out!*** 

http://gbppr.ddns.net/agilent-esa.main.cgi

http://gbppr.ddns.net/agilent-esg.main.cgi
