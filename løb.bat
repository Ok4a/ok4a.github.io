echo off
py -3.14 ALL.py %*
py -3.14 backup.py %*
git add -A
git commit -a -m "New entry added"
git push
pause