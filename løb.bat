echo off
python ALL.py %*
python backup.py %*
timeout /t 10
git commit -a -m "New entry added"
git push
pause