import time
import requests


class Cursus:
    def __init__(self, api) -> None:
        self.__api = api
        
    def get_cursuses(self, user_id):
        """
            /v2/users/:user_id/cursus_users
        """
        resp = requests.post(f"{self.__api.endpoint}/v2/users/{user_id}/correction_points/add", headers=self.__api.header)
        self.__api.eval_resp(resp)
        return resp.json()
    
    def get_cursus(self, user_id, cursus_id : int) -> dict:
        lst = self.get_cursuses(user_id)
        for i in lst:
            if (str(i["cursus_id"]) == cursus_id):
                return i
        return None