#!/bin/bash

BENDER_URL='http://bender:wevJakHeap6@gocept10.gocept.net:8099'
LFODDERS=`curl -s https://intra.gocept.com/intranet/lfodders | awk -F, '{ print $1 ", " $2 ", " $3 }'`
MESSAGE="Wer fetcht heute? ($LFODDERS)"
curl -d "$MESSAGE" $BENDER_URL