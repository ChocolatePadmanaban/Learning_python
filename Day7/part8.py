# Get the total size o

import os
import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
a = completed.stdout.decode('utf-8')
a = a.strip().split("\n")
size = 0
for i in a:
    size += os.stat(i)[6]
print("File size",size)
