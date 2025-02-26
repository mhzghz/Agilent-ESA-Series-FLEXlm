#!/usr/bin/perl

## --> Agilent ESA-Series FLEXlm Crypt Generator, agilent-esa.cgi
## --> Green Bay Professional Packet Radio, www.gbppr.net

# Setup
#
## Program Setup
#
$ENV{PATH} = "/bin:/usr/bin:/usr/local/bin";
select STDOUT;
$| = 1;
use warnings;
require "flush.pl";

## Create a random directory for working files
#
my $sec = 0;
my $min = 0;
my $hour = 0;
my $mday = 0;
my $mon = 0;
my $year = 0;
($sec, $min, $hour, $mday, $mon, $year) = gmtime;
$mon  = sprintf "%02.0f", $mon + 1;
$mday = sprintf "%02.0f", $mday; 
$year = sprintf "%02.0f", $year;
$year = 1900 + $year;

my $RAN = sprintf "%.f", rand(10000000);
mkdir "tmp/$mon-$mday";
mkdir "tmp/$mon-$mday/$RAN";
chdir "tmp/$mon-$mday/$RAN";

#
# Print MIME
#
print "Content-type:text/html\n\n";

# Read environment
#
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $value =~ tr/+/ /;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  $FORM{$name} = $value;
}

$hostid = $FORM{'hostid'};
$option = $FORM{'option'};

# Clean up user input data
#
$hostid =~ tr/A-Za-z0-9//csd;
$option =~ tr/A-Za-z0-9//csd;

if (!$hostid) {
  $hostid = "1301531D";
}

if (!$option) {
  $option = "1DR";
}

print "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 3.2//EN\">".
      "<html>".
      "<head>".
      "<title>Results</title>".
	  "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n".
      "</head>".
      "<body bgcolor=\"#D3D3D3\" text=\"#000000\" link=\"blue\">".
	  "<font face=\"Helvetica\">\n".
      "<center>".
      "<h1>Agilent ESA-Series Spectrum Analyzers<br>FLEXlm Crypt Generator Results</h1>".
      "</center>".
	  "<blockquote>".
	  "<b>Host ID:</b> <font color=\"red\"><tt>$hostid</tt></font><br>\n".
	  "<b>Option:</b> <font color=\"green\"><tt>$option</tt></font>\n";

open(F, ">", "license.lic") or die "Can't open license.lic: $!\n" ;
  print F "FEATURE $option TMOMID01 1.0 permanent uncounted 0123456789AB HOSTID=$hostid\n";
close F;

system("export WINEDEBUG=-all; /usr/bin/wine /usr/local/bin/lmcryptTMOMID01.exe license.lic");

system("/bin/cat license.lic | awk '{print \$7}' > key");

open(F, "<", "key");
 print "<br><b>License Key:</b> <font color=\"blue\"><tt>";
  while(<F>) {
  chomp;
  print;
}
close F;

print "</tt></font>";
print "<pre>This is still kinda <a href=\"https://www.eevblog.com/forum/testgear/enabling-options-on-agilent-esa-series-e4402b-e4404b-e4405b-e4407b/\">experimental</a></pre></blockquote></font></body></html>";
