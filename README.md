lastfm2exfm
===========

"Copy" last.fm loved tracks to ex.fm

Install dependencies:
====

* brew install python3 (for Mac OS X. for Linux must be "<some-pkg-mgr> install python3")
* pip3 install pylast
* pip3 install requests

Configure:
====

* mv ./config.ini.sample ./config.ini
* Fill in config.ini with "real" values (sorry about that for now, but you'll have to obtain last.fm api account here: http://www.last.fm/api/account/create)

Run:
====

* python3 ./move.py

TODOs:
====
* Refactoring
* TODOs in code
* Put it online
* Something completely different
* Most important is to add "page" param to pylast lib's "get_loved_tracks" call, because now it returns some first 50 loved tracks only and that is realy not cool.