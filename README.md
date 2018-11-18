# views



Script to either visit a web page or vote in some online poll a whole bunch of times.  Uses TOR
browser as a pass through local proxy for anonymization and Firefox private browser to avoid
website tracking.  Some sites block TOR exit nodes, so the number of visits/votes specified at
runtime may not reflect the actual number of page visits. This is unavoidable atm.

Currently only supports Strawpoll.me polls.  Add an issue if you find another poll platform you
want added.<br />

The following two directories will be created in the ```views.py``` root directory:<br />
&nbsp;&nbsp;-```logs/```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores session logs as ```sec.log```<br />


**Package requirements:**

&nbsp;&nbsp;colorama
```
pip install colorama
```
&nbsp;&nbsp;selenium
```
pip install selenium
```

**System Requirements:**

&nbsp;&nbsp;python 3

**Usage:**
```
usage: views.py [-h] [-v VISIT_URL] [-p VOTE_URL] [-N NUM]

optional arguments:
  -h, --help    show this help message and exit
  -v VISIT_URL  View this page a whole bunch of times
  -p VOTE_URL   Vote in this poll
  -N NUM        Do it this many times
  
```
