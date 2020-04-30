# uc_pidfile  
A set of classes and functions for managing pidfile.

It is part of the Unicon project

https://unicon.10k.me

#### Using:
```python
import uc_pidfile
```

#### Functions:

**process_exists**(pid)

Checks if the process is running.
Returns True if process exists and False if not.



**read_pid**(filename)

Reads pid from file.

If the file exists and is successfully read,
then returns pid otherwise returns None.

May raise exceptions:
- PermissionError
- ValueError



**validate_pidfile(filename)**

Checks the contents of pidfiles for an integer.

Returns True if valid or False if not.

May raise exceptions:
- FileNotFoundError
- PermissionError



**is_running(filename)**

Returns True if the process is running, otherwise returns False.

It will also be considered that the process is started even if there is no access to the file.
And it will be considered that the process is not started if there is no file or the file contains incorrect data.



#### Classes:

**PidFile(filename, overwrite=False)**

Creates pid file.

If the file already exists and overwrite = True it will be overwritten. But if overwrite = false then this will throw an exception FileExistsError.

May raise exceptions:
- FileExistsError
- PermissionError
- FileNotFoundError (If the target directory does not exist, for example.)