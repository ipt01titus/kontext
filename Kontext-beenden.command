#!/bin/zsh
cd -- "${0:A:h}"
python3 app/launcher.py stop
result=$?
if (( result != 0 )); then
  read "?Zum Schließen Enter drücken."
fi
exit $result
