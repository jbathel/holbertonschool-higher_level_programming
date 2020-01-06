#!/bin/bash
#Script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response
curl -sI http://349bff8a59bb.38.hbtn-cod.io:5000/ | grep -i Content-Length | awk '{ print [ }'' ] }'
