import os
import multiprocessing
_home = os.path.expanduser("~")
chdir = os.path.join(_home, 'websites', 'blogCMS')
bind = '127.0.0.1:4002'
workers = multiprocessing.cpu_count() * 2 + 1
umask = 0o022
loglevel='warning'
timeout=120