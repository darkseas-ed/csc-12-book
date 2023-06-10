#!/usr/bin/env python
"""
Module:      dodo.py
Description: Task runner for the Jupyter Book project
Author:      Gavin Coombes
Date:        10 June 2023

"""
# Imports
from doit.action import CmdAction

# Constants

# Functions

def task_build():
    book = '.'
    task = {
        'actions': [f'jupyter-book build {book}'],
        'doc': 'Build the jupyter book',
        'verbosity': 2,
    }
    return task


def task_push():
    """Push to github pages repo

    https://pypi.org/project/ghp-import/
    """
    cmd_str = 'ghp-import -n -p -f _build/html'
    cwd = 'csc-12-book'
    task = {
        'actions': [cmd_str],
        'verbosity': 2,

    }
    return task
# Tests

if __name__ == "__main__":

    

    print("__done__")
 
