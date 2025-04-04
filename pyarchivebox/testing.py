from main import PyArchiveBox

archivebox = PyArchiveBox("admin", "developementpassword", "http://localhost:8000")

archivebox.login()
archivebox.add("https://www.youtube.com/watch?v=M31DhtoNh9w", "youtube1, youtube", ["media", "title"])
archivebox.add("https://youtu.be/xJzW9-j3BB0?si=4HiO1_lrfazfQ6DN", "youtube", ["media", "title", "favicon"])

title = input("insert the title of the archive you want to delete: ")
date = input("insert the date of the archive you want to delete (exactly how you find it in archivebox): ")
response = archivebox.delete(title, date)

title = input("insert the title of the archive you want to pull: ")
date = input("insert the date of the archive you want to pull (exactly how you find it in archivebox): ")
response = archivebox.pull(title, date)

title = input("insert the title of the archive you want to re-snapshot: ")
date = input("insert the date of the archive you want to re-snapshot (exactly how you find it in archivebox): ")
response = archivebox.re_snapshot(title, date)

title = input("insert the title of the archive you want to reset: ")
date = input("insert the date of the archive you want to reset (exactly how you find it in archivebox): ")
response = archivebox.reset(title, date)

latest = archivebox.get_latest()
print(latest[0])

print("test finished")