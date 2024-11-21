import time
import requests
import json

__all__ = ["Cursus"]

class Cursus:
    def __init__(self, api) -> None:
        self.__api = api
        
    def get_cursuses(self, user_id):
        """
            Returns cursus data of given user_id.
            ARGS:
                user_id (str): User id
            RETURN:
                dict: dictinory
        """
        resp = requests.get(f"{self.__api.endpoint}/v2/users/{user_id}/cursus_users", headers=self.__api.header)
        self.__api.eval_resp(resp)
        return resp.json()
    
    def get_cursus(self, user_id, cursus_id : int) -> dict:
        """
            Returns cursus data of given user_id.
            ARGS:
                user_id (str): User id,
                cursus_id (int): Cursus id
            RETURN:
                dict: dictinory
        """
        lst = self.get_cursuses(user_id)
        for i in lst:
            if (i["cursus"]["id"] == cursus_id):
                return i
        return None