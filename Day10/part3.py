# checking list of files in server

import ftplib
f =ftplib.FTP("ftp.gnu.org","anonymous", "")
files=[]
print(f.retrlines("LIST",files.append))
print(len(files))
print(files[0])