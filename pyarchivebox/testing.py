"""
I didn't yet find out a way to do unit tests on this project as I have to manually verify via the web interface things like if a url was successfully archived ecc...
"""

from main import PyArchiveBox

archivebox = PyArchiveBox("admin", "developementpassword", "0.7.6", "http://localhost:8000")

archivebox.login()
archivebox.add("https://www.youtube.com/watch?v=M31DhtoNh9w", "youtube1, youtube", ["media", "title"])
archivebox.add("https://youtu.be/xJzW9-j3BB0?si=4HiO1_lrfazfQ6DN", "youtube", ["media", "title", "favicon"])

title = input("insert the title of the archive you want to delete: ")
date = input("insert the date of the archive you want to delete (exactly how you find it in archivebox): ")
response = archivebox.delete(title, date)

title = input("insert the title of the archive you want to pull: ")
date = input("insert the date of the archive you want to pull (exactly how you find it in archivebox): ")
response = archivebox.pull(title, date)

print("test finished")