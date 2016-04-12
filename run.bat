@ECHO OFF

:LOOP
ECHO Waiting for 5 minutes...
  PING -n 300 127.0.0.1>nul
  python vigenere.py
GOTO LOOP