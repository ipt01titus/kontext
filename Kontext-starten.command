#!/bin/zsh
cd -- "${0:A:h}"
if ! command -v python3 >/dev/null 2>&1; then
  print "Python 3 mit SQLite wird benötigt. Bitte die Einrichtung mit Codex prüfen."
  read "?Zum Schließen Enter drücken."
  exit 1
fi
python3 app/launcher.py start
result=$?
if (( result != 0 )); then
  read "?Zum Schließen Enter drücken."
fi
exit $result
