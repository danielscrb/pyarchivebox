# pyarchivebox
This package simplifies the process of accessing your archivebox instance trough python.  
It allows you to access your server on version before 0.8.0 where there is no official REST API.

## Docs
You can find the docs on [ReadTheDocs](https://pyarchivebox.readthedocs.io/en/latest/index.html)

## Quick start
To use the package just install the package using `pip`:

```bash
python3 -m pip install pyarchivebox
```

Then make an object of the class containing your login info and server ip/domain:

```python
archivebox = PyArchiveBox("admin", "developementpassword", "http://localhost:8000")
```

Then you have to obtain a session cookie and a csrf token using the login method:

```python
archivebox.login()
```

and you can start using all the package in your project.

## Contributing
All contributions, even small ones like correcting a typo, are welcome. Just make a pull request.