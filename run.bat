@ECHO OFF

:LOOP
ECHO Waiting for 1 minute...
  PING -n 60 127.0.0.1>nul
	ECHO Morse:
	python morse.py
	python morse.py
	ECHO.
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