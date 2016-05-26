#!/usr/bin/python2.7

from paver.easy import *
import paver.doctools
import os
import glob
import shutil

@task
def test():
  sh('nosetests --with-coverage test/test*.py')
  pass

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
  pass

@task
@needs(['clean', 'test'])
def default():
  pass
