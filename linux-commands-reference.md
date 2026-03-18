# 🚀 DevOps Commands Reference

This file contains commands I use during my DevOps learning journey.


# Linux Commands

-> Navigation

    'pwd' - show current directory
    'ls' - list files
    'cd' - change directory


-> File Management

    'mkdir' - create directory
    'touch' - create file
    'rm' - delete file


-> File Viewing

    'cat' - display file content
    'less' - scroll file content
    'head' - first lines of file
    'tail' - last lines of file
    'tail -f' - live logs


-> Searching

    'grep - search text in files
  

-> Permissions

    'ls -l' - view permissions
    'chmod +x file.sh' - make executable
    'chmod 777 file' - full access (not recommended)
    'chmod 644 file' - read/write owner, read others
    'chmod 755 file' - executable with limited write access


-> Terminal Usage

    'history' - show previous commands
    'clear' - clear terminal


## Git Commands

-> Basic Workflow

    'git init' - initialize repo
    'git clone <url>' - clone repository
    'git add .' - stage changes
    'git commit -m "message"' - save changes
    'git push' - upload to GitHub
    'git pull' - get latest changes

-> Branching & Sync
    'git checkout main' - switch branch
    'git branch' - list branches
    'git pull origin main --rebase' - fix conflicts (like : ! [rejected] error: failed to push some refs to)
    'git rebase --continue' - continue rebase

-> Troubleshooting
    'git status' - check changes
    'git log' - view commit history


## File Editing

    'nano filename' - open editor
    'CTRL + X' → exit
    'Y' → save
    'Enter' → confirm

