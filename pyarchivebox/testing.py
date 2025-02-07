"""
I didn't yet find out a way to do unit tests on this project as I have to manually verify via the web interface things like if a url was successfully archived ecc...
"""

from main import PyArchiveBox

archivebox = PyArchiveBox("admin", "developementpassword", "0.7.6", "http://localhost:8000")

archivebox.login()
archivebox.add("https://www.youtube.com/watch?v=M31DhtoNh9w", "youtube1, youtube", ["media", "title"])
archivebox.add("https://youtu.be/xJzW9-j3BB0?si=4HiO1_lrfazfQ6DN", "youtube", ["media", "title", "favicon"])

input("proceed with next action (delete)")

response = archivebox.delete("This is Minecraft. - YouTube", "2025-02-06 9:02PM")