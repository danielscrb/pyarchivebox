# Usage
First you have to import the package

```python
from pyarchivebox import PyArchiveBox
```

Then make an object of the class (be sure to replace the credentials and url with your credentials and url)

```python
archivebox = PyArchiveBox("admin", "password", "localhost:8000")
```

Then you have to use the login method to obtain a session cookie and csrf token

```python
archivebox.login()
```

And then you are ready to go.

## Methods
These are all the methods you can use:

### login()
**parameters**: None  

**returns**: Server response (error codes, ecc...)  

**example**:  
```python
archivebox.login()
```

### add()
**parameters**:  
- ``url`` (str): the url to be archived.
- ``tag`` (str): list of tags to be added to the archive. For more tags separate them with a comma (optional)  
- ``archive_methods`` (list): a list containing all the archive methods. It must contain only strings. (optional)
- ``parser`` (str): wich parser should archivebox use. Use only the ones you find in the webui.
- ``depth`` (int): it can only be 0 or 1. the depth of the links. depth 0 = only the link you give it. depth 1 = the link you give it and the links inside the link  

**returns**: `str` if depth >1. else None  

**example**: 
```python
archivebox.add("https://httpbin.org", "later_use, programming", ["favicon", "singlefile", "title"])
```

### delete()
**parameters**: 
- ``title`` (str): the title of the archive you want to delete
- ``date_added`` (str): the date when the archive you want to delete was added

**returns**: server response

**example**: 
```python
archivebox.delete(title, date)
```

### pull()
**parameters**:
- ``title`` (str): The title of the archive to update snapshots for.
- ``date_added`` (str): The date when the archive was added.

**returns**: Server response indicating success or failure.

**example**:
```python
archivebox.pull(title, date)
```

### re_snapshot()
**parameters**:
- ``title`` (str): The title of the archive to re-snapshot.
- ``date_added`` (str): The date when the archive was added.

**returns**: Server response indicating success or failure.

**example**:
```python
archivebox.re_snapshot(title, date)
```

### reset()
**parameters**:
- ``title`` (str): The title of the archive to reset.
- ``date_added`` (str): The date when the archive was added.

**returns**: Server response indicating success or failure.

**example**:
```python
archivebox.reset(title, date)
```

### get_latest()
**parameters**: None

**returns**: Latest archives as retrieved from the system in the form of a dictionary:
```python
{
    0: {
            "title": archive_title,
            "date_added": archive_date,
            "url": archive_url,
            "size": archive_size
    }
    1: {
            "title": archive_title,
            "date_added": archive_date,
            "url": archive_url,
            "size": archive_size
        }
}
```

**example**:
```python
latest_archives = archivebox.get_latest()
```

