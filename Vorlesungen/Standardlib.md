```python
import sys
```


```python
sys.argv
```




    ['/opt/mambaforge/envs/python310/lib/python3.10/site-packages/ipykernel_launcher.py',
     '-f',
     '/home/pya_trainer_master/.local/share/jupyter/runtime/kernel-b9371707-3ea8-4926-9b79-36c3d7270979.json']




```python
sys.base_prefix
```




    '/opt/mambaforge/envs/python310'




```python
sys.builtin_module_names
```




    ('_abc',
     '_ast',
     '_codecs',
     '_collections',
     '_functools',
     '_imp',
     '_io',
     '_locale',
     '_operator',
     '_signal',
     '_sre',
     '_stat',
     '_string',
     '_symtable',
     '_thread',
     '_tracemalloc',
     '_warnings',
     '_weakref',
     'atexit',
     'builtins',
     'errno',
     'faulthandler',
     'gc',
     'itertools',
     'marshal',
     'posix',
     'pwd',
     'sys',
     'time',
     'xxsubtype')




```python
sys
```




    <module 'sys' (built-in)>




```python
sys.byteorder
```




    'little'




```python
sys.dont_write_bytecode
```




    False




```python
sys.executable
```




    '/opt/mambaforge/envs/python310/bin/python'




```python
sys.flags
```




    sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0, warn_default_encoding=0)




```python
sys.getrecursionlimit()
```




    3000




```python
len(sys.modules)
```




    960




```python
'sys' in sys.modules
```




    True




```python
sys.path
```




    ['/home/pya_trainer_master/data',
     '/opt/mambaforge/envs/python310/lib/python310.zip',
     '/opt/mambaforge/envs/python310/lib/python3.10',
     '/opt/mambaforge/envs/python310/lib/python3.10/lib-dynload',
     '',
     '/opt/mambaforge/envs/python310/lib/python3.10/site-packages',
     '/opt/mambaforge/envs/python310/lib/python3.10/site-packages/IPython/extensions',
     '/home/pya_trainer_master/.ipython']




```python
sys.version
```




    '3.10.1 | packaged by conda-forge | (main, Dec 22 2021, 01:39:05) [GCC 9.4.0]'




```python
sys.version_info
```




    sys.version_info(major=3, minor=10, micro=1, releaselevel='final', serial=0)




```python
v = sys.version_info
```


```python
v.major
```




    3




```python
v.minor
```




    10




```python
sys.stdin
```




    <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>




```python
sys.stdout
```




    <ipykernel.iostream.OutStream at 0x7f848b430fa0>




```python
len(dir(sys))
```




    99




```python
import os
```


```python
len(dir(os))
```




    354




```python
os.altsep
```


```python
os.sep
```




    '/'




```python
os.environ
```




    environ{'USER': 'pya_trainer_master',
            'JUPYTERHUB_OAUTH_SCOPES': '["access:servers!server=pya_trainer_master/", "access:servers!user=pya_trainer_master"]',
            'JUPYTERHUB_HOST': '',
            'JUPYTERHUB_USER': 'pya_trainer_master',
            'HOME': '/home/pya_trainer_master',
            'JUPYTERHUB_SERVICE_URL': 'http://127.0.0.1:44921/ba-ss-2022-01/user/pya_trainer_master/',
            'JUPYTERHUB_OAUTH_CALLBACK_URL': '/ba-ss-2022-01/user/pya_trainer_master/oauth_callback',
            'JUPYTERHUB_API_URL': 'http://127.0.0.1:8081/ba-ss-2022-01/hub/api',
            'JUPYTERHUB_ROOT_DIR': '~/data',
            'JUPYTERHUB_CLIENT_ID': 'jupyterhub-user-pya_trainer_master',
            'PATH': '/opt/mambaforge/envs/python310/bin:/opt/mambaforge/condabin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games',
            'JUPYTERHUB_ACTIVITY_URL': 'http://127.0.0.1:8081/ba-ss-2022-01/hub/api/users/pya_trainer_master/activity',
            'LANG': 'C.UTF-8',
            'SHELL': '/bin/bash',
            'JUPYTERHUB_ADMIN_ACCESS': '1',
            'JUPYTERHUB_SERVICE_PREFIX': '/ba-ss-2022-01/user/pya_trainer_master/',
            'LC_ALL': 'C.UTF-8',
            'JUPYTERHUB_API_TOKEN': '4c65886407a441dcae5fe588aa797a8c',
            'PWD': '/home/pya_trainer_master',
            'JUPYTERHUB_SERVER_NAME': '',
            'JUPYTERHUB_BASE_URL': '/ba-ss-2022-01/',
            'JUPYTERHUB_DEFAULT_URL': '/lab',
            'JPY_API_TOKEN': '4c65886407a441dcae5fe588aa797a8c',
            'JUPYTERHUB_SINGLEUSER_APP': 'jupyter_server.serverapp.ServerApp',
            'PYDEVD_USE_FRAME_EVAL': 'NO',
            'PYTHONUNBUFFERED': '1',
            'JPY_PARENT_PID': '1301',
            'TERM': 'xterm-color',
            'CLICOLOR': '1',
            'PAGER': 'cat',
            'GIT_PAGER': 'cat',
            'MPLBACKEND': 'module://matplotlib_inline.backend_inline'}




```python
os.getpid()
```




    303867




```python
os.geteuid?
```


    [0;31mSignature:[0m [0mos[0m[0;34m.[0m[0mgeteuid[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return the current process's effective user id.
    [0;31mType:[0m      builtin_function_or_method




```python
os.getcwd()
```




    '/home/pya_trainer_master/data'




```python
os.listdir()
```




    ['bbb.txt',
     'erstes.py',
     'Entscheidungen.ipynb',
     'source.zip',
     'IO.ipynb',
     'Scoping.ipynb',
     'wordle_alpha0.2.py',
     'Mengen.ipynb',
     '.virtual_documents',
     'db2.bak',
     'Anweisungen.ipynb',
     'materials',
     'listmath',
     'db2.dat',
     'Datenypen.ipynb',
     'Sequenzen.ipynb',
     'Schleifen.ipynb',
     'liste.pcl',
     'generatoren',
     'db',
     '.ipynb_checkpoints',
     'pylintrc',
     'Objekte.ipynb',
     'scoping.py',
     '__pycache__',
     'Organisation.ipynb',
     'übung4_1_1.py',
     'Bibliothek.ipynb',
     'übung4_1_2.py',
     'Dictionarys.ipynb',
     'Standardlib.ipynb',
     'Syntax.ipynb',
     'io',
     'wordle_alpha_0_3.py',
     'Iteratoren.ipynb',
     'Funktionen.ipynb',
     'Ausnahmen.ipynb',
     'shared',
     'Strings.ipynb',
     'Einführung.ipynb',
     'db2.dir',
     'Klassen.ipynb',
     'admin',
     'data.txt',
     'Listen.ipynb']




```python
os.walk?
```


    [0;31mSignature:[0m [0mos[0m[0;34m.[0m[0mwalk[0m[0;34m([0m[0mtop[0m[0;34m,[0m [0mtopdown[0m[0;34m=[0m[0;32mTrue[0m[0;34m,[0m [0monerror[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mfollowlinks[0m[0;34m=[0m[0;32mFalse[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Directory tree generator.
    
    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple
    
        dirpath, dirnames, filenames
    
    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).
    
    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).
    
    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.
    
    By default errors from the os.scandir() call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.
    
    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.
    
    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.
    
    Example:
    
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
    [0;31mFile:[0m      /opt/mambaforge/envs/python310/lib/python3.10/os.py
    [0;31mType:[0m      function




```python
import time

time.localtime(os.path.getatime('bbb.txt'))
```




    time.struct_time(tm_year=2022, tm_mon=6, tm_mday=7, tm_hour=7, tm_min=50, tm_sec=29, tm_wday=1, tm_yday=158, tm_isdst=0)




```python
%ls -l bbb.txt
```

    -rw-r--r-- 1 pya_trainer_master pya_trainer_master 46 Jun  7 07:52 bbb.txt



```python
os.path.join('a', 'b', 'c')
```




    'a/b/c'




```python
os.path.splitdrive?
```


    [0;31mSignature:[0m [0mos[0m[0;34m.[0m[0mpath[0m[0;34m.[0m[0msplitdrive[0m[0;34m([0m[0mp[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Split a pathname into drive and path. On Posix, drive is always
    empty.
    [0;31mFile:[0m      /opt/mambaforge/envs/python310/lib/python3.10/posixpath.py
    [0;31mType:[0m      function




```python
import shutil
```


```python
shutil?
```


    [0;31mType:[0m        module
    [0;31mString form:[0m <module 'shutil' from '/opt/mambaforge/envs/python310/lib/python3.10/shutil.py'>
    [0;31mFile:[0m        /opt/mambaforge/envs/python310/lib/python3.10/shutil.py
    [0;31mDocstring:[0m  
    Utility functions for copying and archiving files and directory trees.
    
    XXX The functions here don't copy the resource fork or other metadata on Mac.




```python
shutil.get_terminal_size
```




    <function shutil.get_terminal_size(fallback=(80, 24))>




```python
from pathlib import Path
```


```python
p = Path()
```


```python
p
```




    PosixPath('.')




```python
p.absolute()
```




    PosixPath('/home/pya_trainer_master/data')




```python
p / 'x'
```




    PosixPath('x')




```python
Path.__truediv__??
```


    [0;31mSignature:[0m [0mPath[0m[0;34m.[0m[0m__truediv__[0m[0;34m([0m[0mself[0m[0;34m,[0m [0mkey[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m <no docstring>
    [0;31mSource:[0m   
        [0;32mdef[0m [0m__truediv__[0m[0;34m([0m[0mself[0m[0;34m,[0m [0mkey[0m[0;34m)[0m[0;34m:[0m[0;34m[0m
    [0;34m[0m        [0;32mtry[0m[0;34m:[0m[0;34m[0m
    [0;34m[0m            [0;32mreturn[0m [0mself[0m[0;34m.[0m[0m_make_child[0m[0;34m([0m[0;34m([0m[0mkey[0m[0;34m,[0m[0;34m)[0m[0;34m)[0m[0;34m[0m
    [0;34m[0m        [0;32mexcept[0m [0mTypeError[0m[0;34m:[0m[0;34m[0m
    [0;34m[0m            [0;32mreturn[0m [0mNotImplemented[0m[0;34m[0m[0;34m[0m[0m
    [0;31mFile:[0m      /opt/mambaforge/envs/python310/lib/python3.10/pathlib.py
    [0;31mType:[0m      function




```python
b = Path('bbb.txt')
```


```python
b
```




    PosixPath('bbb.txt')




```python
b.read_text()
```




    'https://b3.python-academy.de/b/mik-fg6-v6f-4ma'




```python
import datetime
```


```python
d = datetime.datetime(2006, 4, 12)
```


```python
d
```




    datetime.datetime(2006, 4, 12, 0, 0)




```python
d.month
```




    4




```python
t = datetime.datetime.today()
```


```python
t
```




    datetime.datetime(2022, 6, 8, 15, 37, 42, 615742)




```python
t - d
```




    datetime.timedelta(days=5901, seconds=56262, microseconds=615742)




```python
diff = t - d
```


```python
diff.total_seconds()
```




    509902662.615742




```python
d14 = datetime.timedelta(days=14)
```


```python
t + d14
```




    datetime.datetime(2022, 6, 22, 15, 37, 42, 615742)




```python
now = datetime.datetime.now()
twentyfour_hours_ago = now - datetime.timedelta(1)
path = "/usr/lib/"
print(now, twentyfour_hours_ago)
for file in [os.path.join(dp, f) for dp, dn, fn in os.walk(path) for f in fn]:
#for file in os.walk("/"):
    print(file)
    if os.path.getatime(file) >= twentyfour_hours_ago.timestamp():
        print(file)
```


```python
now
```




    datetime.datetime(2022, 6, 8, 16, 37, 7, 166364)




```python
twentyfour_hours_ago
```




    datetime.datetime(2022, 6, 7, 16, 37, 7, 166364)




```python
twentyfour_hours_ago.timestamp()
```




    1654619827.166364




```python
os.walk?
```


    [0;31mSignature:[0m [0mos[0m[0;34m.[0m[0mwalk[0m[0;34m([0m[0mtop[0m[0;34m,[0m [0mtopdown[0m[0;34m=[0m[0;32mTrue[0m[0;34m,[0m [0monerror[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mfollowlinks[0m[0;34m=[0m[0;32mFalse[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Directory tree generator.
    
    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple
    
        dirpath, dirnames, filenames
    
    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).
    
    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).
    
    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.
    
    By default errors from the os.scandir() call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.
    
    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.
    
    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.
    
    Example:
    
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
    [0;31mFile:[0m      /opt/mambaforge/envs/python310/lib/python3.10/os.py
    [0;31mType:[0m      function




```python
now = datetime.datetime.now()
ago = (now - datetime.timedelta(minutes=30)).timestamp()
path = "."
for root, dirs, files in os.walk(path):
    for file in files:
        full_name = os.path.join(root, file)
        if os.path.getatime(full_name) >= ago:
            print(full_name)
```

    ./Standardlib.ipynb
    ./.virtual_documents/Standardlib.ipynb
    ./.virtual_documents/shared/übung22.ipynb



```python

```
