@ECHO OFF

:LOOP
ECHO Waiting for 5 minutes...
  PING -n 300 127.0.0.1>nul
	ECHO Vigenere:
  python vigenere.py
	ECHO.
	ECHO Caesar:
	python caesar.py
	ECHO.
	ECHO Playfair:
	python playfair.py
	ECHO.
	ECHO.
GOTO LOOP