#!/bin/zsh
cd -- "${0:A:h}"

kontext_pilot_data="/tmp/kontext-pilot-qa"
if [[ ! -f "$kontext_pilot_data/kontext.sqlite3" ]]; then
  print "Der bisherige Kontext-Testbestand wurde nicht gefunden. Es wurde nichts verändert."
  read "?Zum Schließen Enter drücken."
  exit 1
fi

# Den vorhandenen Bestand zusätzlich sichern und denselben Dienst neu laden.
python3 -B - <<'PY'
from app.storage import Store
Store('/tmp/kontext-pilot-qa').backup()
print('Der bisherige Kontext-Bestand wurde zusätzlich gesichert.')
PY
result=$?
if (( result == 0 )); then
  python3 -B app/launcher.py stop --port 8775 --data-dir "$kontext_pilot_data"
  result=$?
fi
if (( result == 0 )); then
  python3 -B app/launcher.py start --port 8775 --data-dir "$kontext_pilot_data"
  result=$?
fi
if (( result != 0 )); then
  print "Der Neustart wurde nicht abgeschlossen. Bitte diese Ausgabe an Codex weitergeben."
  read "?Zum Schließen Enter drücken."
fi
exit $result
