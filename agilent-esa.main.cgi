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
<title>Agilent ESA/ESG-Series FLEXlm Crypt Generator</title>
</head>
<body bgcolor="#D3D3D3" text="#000000" link="blue">
<font face="Helvetica">

<center>
<table border="10" cellpadding="8">
<tr>
<td bgcolor="#A3A3A3"><font size="10" face="Helvetica" color="#82007C"><b><center>Agilent ESA-Series Spectrum Analyzer<br>Agilent ESG-Series Signal Generator<br>FLEXlm Crypt Generator</center></b></font></td>
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
<option>[ESA Options]</option>
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
<option>[ESG Options]</option>
<option>100</option>
<option>101</option>
<option>200</option>
<option>201</option>
<option>202</option>
<option>404</option>
<option>406</option>
<option>300</option>
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

<br>
<hr>
<br>

<blockquote>
<p>Pre-made personality ZIP files.&nbsp;&nbsp;Extract the contents of these files using <a href="https://en.wikipedia.org/wiki/WinZip">WinZip</a>/<a href="agilent/pkunzip.exe">PKUNZIP</a> to a formatted 3.5-inch floppy disk and run the installation process on your spectrum analyzer.</p>

<ul>
<li><a href="agilent/J35-FMDev-B0102.zip">J35 - FM Deviation - B.01.02</a>&nbsp;&nbsp;(Minimum Firmware: A.07.05, Requires a License Key and Option BAA)&nbsp;&nbsp;[<a href="https://www.keysight.com/us/en/lib/software-detail/instrument-firmware-software/esa-fm-deviation-measurements-option-j35j36-1000001084epsgsud.html">Agilent Info</a>]</li>

<p></p>

<li><a href="agilent/219-NoiseFigure-A0107-1.zip">219 - Noise Figure - A.01.07 - Disk #1</a>&nbsp;&nbsp;(Minimum Firmware: A.12.00, Requires a License Key and Options B72, 1DS, <a href="agilent/219-NoiseFigure-A0107-2.zip">Disk #2</a>)&nbsp;&nbsp;[<a href="https://www.keysight.com/us/en/lib/software-detail/instrument-firmware-software/esa-noise-figure-measurement-personality-option-219-420400.html">Agilent Info</a>, <a href="agilent/219-NoiseFigure.pdf">Manual</a>]</li>

<p></p>

<li><a href="agilent/225-CableFault-B0104.zip">225 - Cable Fault Location - B.01.04</a>&nbsp;&nbsp;(Minimum Firmware: A.07.01, Requires a License Key and Options B72, 1DN)&nbsp;&nbsp;[<a href="https://www.keysight.com/us/en/lib/software-detail/instrument-firmware-software/esa-cable-fault-location-measurement-personality-option-225-1000000940epsgsud.html">Agilent Info</a>, <a href="agilent/225-CableFault.pdf">Manual</a>]</li>

<p></p>

<li><a href="agilent/226-PhaseNoise-B0131.zip">226 - Phase Noise Utility - B.01.31</a>&nbsp;&nbsp;(Minimum Firmware: A.08.02, Requires a License Key and Option B72)&nbsp;&nbsp;[<a href="https://www.keysight.com/us/en/lib/software-detail/instrument-firmware-software/esa-phase-noise-measurement-personality-option-226-1000001091epsgsud.html">Agilent Info</a>, <a href="agilent/226-PhaseNoise.pdf">Manual</a>]</li>

<p></p>

<li><a href="agilent/229-ModulationAnalysis-A0202-1.zip">229 - Modulation Analysis - A.02.02 - Disk #1</a>&nbsp;&nbsp;(Minimum Firmware: A.08.04, Requires a License Key and Options B72, B7D, B7E, 1D5, Includes Option 231, <a href="agilent/229-ModulationAnalysis-A0202-2.zip">Disk #2</a>)&nbsp;&nbsp;[<a href="https://www.keysight.com/us/en/lib/software-detail/instrument-firmware-software/esa-modulation-analysis-measurement-personality-option-229-1000001047epsgsud.html">Agilent Info</a>]</li>

<p><p>

<li><a href="agilent-esg.main.cgi"><b>Agilent ESG-Series Signal Generator FLEXlm Crypt Generator</b></a></li>
</ul>
</blockquote>
</font>
</body>
</html>
EOF
