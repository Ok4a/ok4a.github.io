echo off
python ALL.py %*
python backup.py %*
git commit -a -m "New entry added"
git add
git push
pause