# to execute inix commands in python
# https://pymotw.com/3/subprocess/index.html

import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)

import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)