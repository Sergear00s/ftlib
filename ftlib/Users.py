import requests
class Users:
    def __init__(self, api) -> None:
        self.__api = api

    def get_user_id_by_login(self, login : str) -> int:
        """
            login: user login,
            return value: user id
        """
        if (self.__api.token_check() is False):
            self.__api.update_token()
        params = {"filter[login]": login, "filter[primary_campus_id]": self.__api.campus_id}
        resp = requests.get(f"{self.__api.endpoint}/v2/users", params=params, headers=self.__api.header)
        self.__api.eval_resp(resp)
        jsn = resp.json()
        if (jsn and len(jsn)>0):
            return int(jsn[0]["id"])
        return 0