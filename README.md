# views



Script to either visit a web page or vote in some online poll a whole bunch of times.  Uses TOR
browser as a pass through local proxy for anonymization and Firefox private browser to avoid
website tracking.  Some sites block TOR exit nodes, so the number of visits/votes specified at
runtime may not reflect the actual number of page visits. This is unavoidable atm.

Currently only supports Strawpoll.me polls.  Add an issue if you find another poll platform you
want added.

Not super fast (approx. 1 visit/vote per 3-5 seconds).  This is a consequence of your network speed and
the disgustingly bloated size of modern websites.<br />

The following directory will be created in the ```views.py``` root directory:<br />
&nbsp;&nbsp;-```logs/```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores session logs as ```sec.log```<br />


**Package requirements:**

&nbsp;&nbsp;install requirements
```
pip install -r requirements.txt
```

**System Requirements:**

&nbsp;&nbsp;python 3<br />
&nbsp;&nbsp;TOR Browser<br />
&nbsp;&nbsp;TOR Service<br />
&nbsp;&nbsp;Current GeckoDriver for Firefox (https://github.com/mozilla/geckodriver)<br />
&nbsp;&nbsp;GeckoDriver executable filepath in ```PATH```<br />

**Config**

&nbsp;&nbsp;Add filepath to ```start-tor-browser``` executable to the ```src/views.conf``` file<br />

**Usage:**
```
usage: views.py [-h] [-v VISIT_URL] [-p VOTE_URL] [-N NUM]

optional arguments:
  -h, --help    show this help message and exit
  -v VISIT_URL  View this page '-N' times
  -p VOTE_URL   Vote in this poll '-N' times
  -N NUM        Do it this many times
  
```
