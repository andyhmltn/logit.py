Logit.py
-------------

A dead simple python logger. This will log activity to `~/.logit/` (future releases will allow you to change the path)

Usage
-------------
To use Logger, initiate the class and then call `record` passing in an event (eg: `error`,`warning`,`chicken` that will be displayed before the event in the log file ([ERROR] Example)) like so:

	from logit import Logit

	logger = Logit('My Application Name')
	logger.record('ERROR', 'There was an error onboard!')

Current Version
----------------
Logit.py is currently on version: `0.0.1`.

LICENSE
----------------
The MIT License (MIT)

Copyright (c) 2013 Andy Hamilton (@ FINEIO)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.