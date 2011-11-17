#!/bin/bash

if [ $# -lt 1 ]; then
  echo 1>&2 "Usage: $0 http://user:pass@host"
  exit 1
fi

BENDER_URL=$1
LFODDERS=`curl -s https://intra.gocept.com/intranet/lfodders | awk -F, '{ print $1 ", " $2 ", " $3 }'`
MESSAGE="Wer fetcht heute? ($LFODDERS)"
curl -d "$MESSAGE" $BENDER_URL