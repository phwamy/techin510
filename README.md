# techin510

# Git config

## To view the SSH public key on macOS

```
cat ~/.ssh/id_rsa.pub
```


## To copy the SSH public key on macOS
```
at ~/.ssh/id_rsa.pub | pbcopy
```


## Getting Started
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt --quiet
```

## Content Markdown (About Me)
1. A profile picture
2. About
3. Education
4. Work Experience
5. Hobbies and Interests
6. Interesting Projects

## Git
```
git status
git add .
git commit -m "Upload README.md and app.py"
git rm -r --cached venv
git commit -m "Remove virtual environment from tracking"
git push origin main
```

## Ensure your local branch is up-to-date with the remote branch
```
git pull origin
```


## If the workspace is out-of-syn, fetch and merge change fist
```
git fetch origin

# merge
git merge origin/main

# rebase
git rebase origin/your-branch-name
```