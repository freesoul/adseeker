# adseeker

This software aims to web-scrap several websites (currently only www.milanuncios.es) to find interesting and recent advertisements, and collects the contact information.

The intention is that we automatically send a Whatsap saying that we are interested, so we can catch the most recent opportunities.


## Requisites

### Making Chrome & ChromeDriver undetectable to Distil technology (only headed version for now)

1. You need a stable version of google-chrome-stable installed WHICH HAS NOT 'NavigatorAutomationInformation' implemented. 
After almost becoming crazy trying to find how to remove the 'navigator.webdriver' tag, it was really simple.
That property is set at runtime by a method webdriver() which always return true, as long as 'webdriver' is visible in the Navigator interface scope.
I did not notice how did worked until I found a google group where they put a link to the commit that incorporated all changes to accomplish with
W3C rules for webdrivers, that means, incorporating 'NavigatorAutomationInformation' to the prototype.

That means you have two options here:

	1.A. Recompile the last version of chromium (probably "no, thanks")
		1.A.1. Download the source (https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions.md#System-requirements)
		1.A.2. Modify 'third_party/WebKit/Source/core/frame/Navigator.idl' by commenting the line 'Navigator implements NavigatorAutomationInformation';
		1.A.3. Start compiling it in your super-computer and go on holidays. When you are back maybe it will be built.

	1.B. Use a version which hasn't commited that change yet. That means, anything uploaded *before Oct 2017* (ej. v61).
		1.B.1. Find deb package mirros using 'inurl:/deb/pool/main/g/google-chrome-stable/' at Google.



2. You need to install an also patched version of ChromeDriver at '/usr/bin/local'.

Well, they look for $cdc_... document variable names, and they catch you if there's one. ChromeDriver put one of these, so we have to change it.

	2.A. Download ChromeDriver sourcecode (available in the Chromium source code too, downloadable with depot_tools). (I'd go for 2.B).
		2.A.1. Find the file 'call_function.js' and replace the line 'var key = '$cdc_asdjflasutopfhvcZLmcfl_';' with 'var key = 'sex_and_whisky_';
		2.A.2. Compile it and move it to the folder we said.
	

	2.B. Download ChromeDriver binary for a version which fits the chrome binary. (eg. for chrome v61, we download v2.34, see 
	http://chromedriver.chromium.org/downloads, https://chromedriver.storage.googleapis.com/index.html?path=2.34/)
		2.B.1. Open it with an hex editor and do the step 2.A.1.


### Libraries

Python dependencies:

1. python3 -m pip install beautifulsoup4



## To do

- Read configs from json
- Add whatsap messaging
- Add other modules
