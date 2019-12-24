#!/usr/bin/python3
print()

from git import Repo
repo = Repo("./")
repo.git.add(update=True)
repo.index.commit("python")
origin = repo.remote(name='origin')
origin.push()
