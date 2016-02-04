#!/bin/env python
# coding: utf-8

import subprocess as sp
import sys

SCM = "git"

def stdout(cmd):
  return [
      i
      for i in sp.check_output(cmd).split(b'\n')
      if i
  ]

def check_SCM():
  p = stdout(['pwd'])
  for line in p:
    if "hg" in p:
      SCM = "hg"
      return

def get_staged_files():
  if SCM is "git":
    p = stdout(['git', 'status', '--porcelain'])
  else:
    p = stdout(['hg', 'status'])

  files = []
  for line in p:
    status, filepath = line[:2], line[3:].strip()
    # status: [StagedState UnstagedState]
    # (M)odified (A)dded (D)eleted (?)Untracked
    # [M ] means modified and staged for commit.
    # [ M] means modified but not staged for commit.
    # [AM] means staged added, and unstaged modified.
    # Mercurial not specified staged/unstaged
    if status == 'A ' or status == 'M ':
      files.append(filepath)
  return files

def main():
  result = 1

  for f in get_staged_files():
    if f == "ChangeLog":
      result = 0

  return result

if __name__ == '__main__':
  sys.exit(main())

