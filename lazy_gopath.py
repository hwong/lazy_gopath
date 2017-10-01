#!/usr/bin/env python

import os
import os.path

def lazy_gopath():
    p = os.path.normpath(os.getcwd())
    try:
        i = p.rindex("/src/github.com")
        print p[:i],
    except ValueError as e:
        pass

if __name__ == '__main__':
    lazy_gopath()
