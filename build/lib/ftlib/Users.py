import requests
class Users:
    def __init__(self, api) -> None:
        self.api = api

    def get_user_id_by_login(self, login : str) -> int:
        """return type int
        """
        if (self.api.token_check() is False):
            self.api.update_token()
        params = {"filter[login]": login, "filter[primary_campus_id]": self.api.campus_id}
        resp = requests.get(f"{self.api.endpoint}/v2/users", params=params, headers=self.api.header)
        if (resp.status_code == 200):
            jsn = resp.json()
            if (jsn):
                if (jsn[0]):
                    return int(jsn[0]["id"])
        return 0