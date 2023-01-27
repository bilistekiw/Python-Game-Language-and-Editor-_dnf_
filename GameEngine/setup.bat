@echo off
title Set


:INFO
echo set the pack
echo press any key...
pause>nul

:INSTALL
cls
echo set...
pip3 install pywin32
cls
echo set...
pip3 install --upgrade pywin32
cls
echo set...
pip3 install wxpython
cls
echo set...
pip3 install --upgrade wxpython
cls
echo set...
pip3 install easygui
cls
echo set...
pip3 install --upgrade easygui
cls

:FINISH
echo Ok set
echo Press any key...
pause>nul
exit