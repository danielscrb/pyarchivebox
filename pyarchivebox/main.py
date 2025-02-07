import requests
from selectolax.parser import HTMLParser

class PyArchiveBox:
    def __init__(self, username: str, password: str, archivebox_url: str):
        self.username = username
        self.password = password
        self.url = archivebox_url
        self.session = requests.Session()
        
        # declare empty variables in __init__ for clarity
        self.csrf_token = None
        self.session_cookie = None

    def __get_archiveid(self, title: str, date_added: str):
        session = self.session
        url = self.url + f"/admin/core/snapshot/?q={title}"

        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }
        page = session.get(url, headers=headers)
        html = HTMLParser(page.text)

        for row in html.css("table#result_list tbody tr"):
            checkbox = row.css_first("td.action-checkbox input[name='_selected_action']")
            archive_id = checkbox.attributes["value"] if checkbox else None

            archive_title = row.css_first("td.field-title_str .status-fetched").text(strip=True) if row.css_first("td.field-title_str") else None
            archive_date = row.css_first("th.field-added").text(strip=True) if row.css_first("th.field-added") else None

            if archive_id and archive_title and archive_date:
                if archive_title == title and archive_date == date_added:
                    return archive_id

    def login(self):
        login_url = self.url + "/admin/login/?next=/"

        session = self.session

        session.get(login_url)
        if "csrftoken" in session.cookies:
            self.csrf_token = session.cookies["csrftoken"]
        elif "csrf" in session.cookies:
            self.csrf_token = session.cookies["csrf"]
        else:
            print("no csrf cookie found")

        payload = {
            "csrfmiddlewaretoken": self.csrf_token,
            "username": self.username,
            "password": self.password
        }

        response = session.post(login_url, data=payload, allow_redirects=True)

        if response.status_code == 200:
            self.session_cookie = session.cookies.get("sessionid")

        return response
    
    def add(self, url: str, tag: str = "", archive_methods: list = [], parser: str = "auto", depth: int = 0):
        add_url = self.url + "/add/"

        session = self.session

        if depth > 1:
            return "cannot have depth over 1"
        else:
            payload = {
                "csrfmiddlewaretoken": self.csrf_token,
                "url": url,
                "parser": parser,
                "tag": tag,
                "depth": depth
            }

            if archive_methods != []:
                payload["archive_methods"] = archive_methods

        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }

        session.post(add_url, data=payload, headers=headers, allow_redirects=True)
    

    def delete(self, title: str, date_added: str):
        session = self.session
        snapshots_url = self.url + f"/admin/core/snapshot/?q={title}"
        archive_id = self.__get_archiveid(title, date_added)
        
        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }
        payload = {
            "csrfmiddlewaretoken": f"{self.csrf_token}",
            "action": "delete_snapshots",
            "select_across": 0,
            "index": 0,
            "_selected_action": f"{archive_id}"
        }
        response = session.post(snapshots_url, data=payload, headers=headers)
        return response
    
    
    def pull(self, title: str, date_added: str):
        session= self.session
        snapshots_url = self.url + f"/admin/core/snapshot/?q={title}"
        archive_id = self.__get_archiveid(title, date_added)

        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }
        payload = {
            "csrfmiddlewaretoken": f"{self.csrf_token}",
            "action": "update_snapshots",
            "select_across": 0,
            "index": 0,
            "_selected_action": f"{archive_id}"
        }
        response = session.post(snapshots_url, data=payload, headers=headers)
        return response
    

    def re_snapshot(self, title: str, date_added: str):
        session = self.session
        snapshots_url = self.url + f"/admin/core/snapshot/?q={title}"
        archive_id = self.__get_archiveid(title, date_added)

        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }
        payload = {
            "csrfmiddlewaretoken": f"{self.csrf_token}",
            "action": "resnapshot_snapshot",
            "select_across": 0,
            "index": 0,
            "_selected_action": f"{archive_id}"
        }
        response = session.post(snapshots_url, data=payload, headers=headers)
        return response
    

    def reset(self, title: str, date_added: str):
        session = self.session
        snapshots_url = self.url + f"/admin/core/snapshot/?q={title}"
        archive_id = self.__get_archiveid(title, date_added)

        headers = {
            "Cookie": f"csrftoken={self.csrf_token}; sessionid={self.session_cookie}; GMT_OFFSET=60"
        }
        payload = {
            "csrfmiddlewaretoken": f"{self.csrf_token}",
            "action": "overwrite_snapshots",
            "select_across": 0,
            "index": 0,
            "_selected_action": f"{archive_id}"
        }
        response = session.post(snapshots_url, data=payload, headers=headers)
        return response