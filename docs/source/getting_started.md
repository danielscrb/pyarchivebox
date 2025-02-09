# Getting started
## Installation
To install the package just use `pip` and install `pyarchivebox`.

```bash
pip install pyarchivebox
```

or 

```bash
python3 -m pip install pyarchivebox
```

## Initialization
To start using the package you first have to make an object of the class `PyArchiveBox`.

In the construtor you must put an username, password for logging in and the url of the server.

```python
archivebox = PyArchiveBox("admin", "developementpassword", "http://localhost:8000")
```

and then you have to login to obtain a session cookie and a csrf token

```python
archivebox.login()
```

After this is done you can start using all of it's methods. (See [Usage](usage.md) for a better explanation)