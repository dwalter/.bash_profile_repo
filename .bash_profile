# general aliases
alias bb='cd ..'
alias jn='jupyter notebook'

# conda
# conda and pip aliases
alias ca="conda activate"
alias condael="conda env list"
condac() {
    conda create -n "$1"
}
condaer() {
    conda env remove -n "$1"
}

#
# GIT ALIASES
#
# alias gs="git status"
alias gs="python ~/git_reverse.py"
alias gd="git diff"
alias gp="git push origin HEAD"
alias ga="git add"
alias gc="git commit -am"
alias gcm="git commit -m"
alias gch="git checkout"
alias gchb="git checkout -b"
alias gb="git branch"
alias gb0="git rev-parse --abbrev-ref HEAD" # prints current branch
alias gl="git log --oneline"
alias gbd="git branch -D"
alias gpull="git pull"
alias gcp="git cherry-pick"
alias gpf="git push --force"

gri() {
    git rebase -i HEAD~"$1"
}

grs() {
    git reset --soft HEAD~"$1";
    git reset;
}

gcf() {
    git commit --fixup HEAD~"$1";
}
