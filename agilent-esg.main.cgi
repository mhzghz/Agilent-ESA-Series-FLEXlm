#!/usr/bin/perl

## --> Agilent ESG-Series FLEXlm Crypt Generator, agilent-esg.main.cgi
## --> Green Bay Professional Packet Radio, www.gbppr.net

# Setup
#
select STDOUT;
$| = 1;

# Print MIME
#
print "Content-type:text/html\n\n";

# Draw me a web page
#
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
<head>
<title>Agilent ESG-Series FLEXlm Crypt Generator</title>
</head>
<body bgcolor="#D3D3D3" text="#000000" link="blue">
<font face="Helvetica">

<center>
<table border="10" cellpadding="8">
<tr>
<td bgcolor="#A3A3A3"><font size="10" face="Helvetica" color="#82007C"><b><center>Agilent ESG-Series Signal Generator<br>FLEXlm Crypt Generator</center></b></font></td>
</tr>
</table>
</center>

<br>
<br>
<br>

<form action="./agilent-esg.cgi" method="post">

<center>
<table border="0">
<tr>
<td><b>Enter Your Host ID :</b></td>
<td><input type="text" name="hostid" size="10" value="9AA2A55F"></td>
</tr>

<tr><td align="right"><b>Select an Option:</b></td>
<td><select name="option">
<option selected>100</option>
<option>101</option>
<option>200</option>
<option>201</option>
<option>202</option>
<option>404</option>
<option>406</option>
<option>300</option>
<option>H97</option>
<option>UN5</option>
<option>UN7</option>
</select></td><td></td></tr>

</table>

<br>
<br>

<table border="2" cellpadding="10">
<tr>
<p><font color="red">Only Press <b>Submit</b> Once!</font><br>Press <b>Submit</b> to see an example.<br><i>It will take up to 30 seconds for program to complete.</i></p>
<td bgcolor="#3240A8"><input type="submit" value="Submit"></td>
<td bgcolor="#3240A8"><input type="reset" value="Clear"></td>
</tr>
</table>
</center>
</form>

<blockquote>
<ul>
<li>1E5 = High-Stability Timebase</li>
<li>H97 = Multi-Channel Wideband-CDMA</li>
<li>UND = Internal Dual Arbitrary Waveform Generator</li>
<li>UN5 = Multi-Channel CDMA</li>
<li>UN7 = Internal Bit-Error-Rate Analyzer</li>
<li>UN8 = Real-Time I/Q Baseband Generator with 1 MB RAM</li>
<li>UN9 - Add 7 MB RAM to Option UN8</li>
<li>100 = ARB Multi-Channel 3GPP and 1.0 W-CDMA (Requires Option UND)</li>
<li>101 = ARB Multi-Channel CDMA2000</li>
<li>200 = Fully-Coded 3GPP Wideband-CDMA (Requires Option UN8)</li>
<li>201 = Real-Time Multi-Channel CDMA2000 (Requires Option UN8)</li>
<li>202 = Enhanced Data Rates for GSM Evolution (EDGE)</li>
<li>300 = GSM/EDGE Loopback Bit Error Rate Tester</li>
</ul>

</font>
</body>
</html>
EOF
