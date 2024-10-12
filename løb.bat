echo off
python ALL.py %*
python backup.py %*
git add -A
git commit -a -m "New entry added"
git push
pause