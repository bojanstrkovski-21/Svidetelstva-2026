#!/bin/bash
# Template: push.sh
# Usage: Run from your repo root to pull, add, commit, and push changes.

echo "Checking for newer files online first"
git pull

# Backup everything inside the project folder
git add --all .

echo "####################################"
echo "Write your commit comment!"
echo "####################################"
read input

git commit -m "$input"

# Push to the correct branch
git config --get remote.origin.url | grep -q main && {
    echo "Using main"
    git push -u origin main
}
git config --get remote.origin.url | grep -q master && {
    echo "Using master"
    git push -u origin master
}

#git push -u origin main --force

echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"
