#!/usr/bin/perl

## --> Agilent ESA-Series FLEXlm Crypt Generator, agilent-esa.main.cgi
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
<title>Agilent ESA-Series FLEXlm Crypt Generator</title>
</head>
<body bgcolor="#D3D3D3" text="#000000" link="blue">
<font face="Helvetica">

<center>
<table border="10" cellpadding="10">
<tr>
<td bgcolor="#A3A3A3"><font size="12" face="Helvetica" color="#82007C"><b><center>Agilent ESA-Series Spectrum Analyzers<br>FLEXlm Crypt Generator</center></b></font></td>
</tr>
</table>
</center>

<br>
<br>
<br>

<form action="./agilent-esa.cgi" method="post">

<center>
<table border="0">
<tr>
<td><b>Enter Your Host ID :</b></td>
<td><input type="text" name="hostid" size="10" value="1301531D"></td>
</tr>

<tr><td align="right"><b>Select an Option:</b></td>
<td><select name="option">
<option>060</option>
<option>106</option>
<option>219</option>
<option>225</option>
<option>226</option>
<option>227</option>
<option>228</option>
<option>229</option>
<option>231</option>
<option>252</option>
<option>304</option>
<option>1D5</option>
<option>1D6</option>
<option>1D7</option>
<option>1DN</option>
<option>1DR</option>
<option>1DS</option>
<option selected>1DR</option>
<option>A4H</option>
<option>AYQ</option>
<option>AYX</option>
<option>AYZ</option>
<option>BAA</option>
<option>BAC</option>
<option>BAH</option>
<option>BBA</option>
<option>B70</option>
<option>B7B</option>
<option>B7K</option>
<option>UKB</option>
</select></td><td></td></tr>

</table>

<br>
<br>

<table border="2" cellpadding="10">
<tr>
<p>Press <b>Submit</b> to see an example.</p>
<td bgcolor="#3240A8"><input type="submit" value="Submit"></td>
<td bgcolor="#3240A8"><input type="reset" value="Clear"></td>
</tr>
</table>
</center>
</form>

</font>
</body>
</html>
EOF
