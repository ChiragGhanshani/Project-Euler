#!/usr/bin/python3

from paver.easy import *
import paver.doctools
import os
import glob
import shutil

@task
def test():
  sh('nosetests --with-coverage test/*.py')
  pass

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
  for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
  pass

@task
@needs(['clean', 'test'])
def default():
  pass
