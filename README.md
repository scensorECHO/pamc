<h1>Python Asset Management Comparator</h1>

<p>This script analyzes an exported semicolon delimited spreadsheet containing asset information
provided to the Asset Manager service. Its purpose is to parse relevant user and location data. </p>

<p>In order to run this code, there are several requirements:
<ul>
<li>a working installation of the Python 2.7.9 runtime environment
<li>an exported template from the Asset Manager, template BEASSETUSER
<li>the standardized lease portfolio provided on the IT department drive
<li>The following file structure in the local script folder: 
  <ul>
  <li>file:	compareassets.py (The script)
	<li>file:	assetkeys (Provided comma-delimited file for assetkeys list)
	<li>file:	exportkeys (Provided comma-delimited file for exportkeys list)
	<li>file:	assetsexport.csv (Exported template from Asset Manager)
	<li>file:	assetstosearch.csv (Portfolio from the department drive)
	<li>note:	Files must be present or the program will not run.
	<li>note:	Copy the portfolio file from the Y drive. The program was designed to be run from the local folder without any access to network drives, or anything pertaining specifically to the user running the script. 
  </ul>
</ul></p>

In the future I expect to update this script to access missing user information through several
different methods, such as:
<ul>
<li>Active Directory queries
<li>PsTools (PsLoggedOn)
<li>Ping / nslookup
</ul>

This script is designed around these specific templates, any changes to column locations will 
also break the functionality of this script as well, although this is to be fixed using key 
generation through analysis, rather than the preordained assetkeys file that is required.

<h1>License</h1>
pamc is released under GNU GPLv3 License.
<br>
Copyright © 2015 Thomas Carrio
