import time
import requests
import json

__all__ = ["Cursus"]

class Cursus:
    def __init__(self, api) -> None:
        self.__api = api
        
    def get_user_cursus(self, user_id : str) -> list:
        "GET /v2/users/:user_id/cursus_users"
        resp = self.__api.Api.page("/v2/users/{}/cursus_users".format(user_id))
        keyss = resp.keys()
        rtn = []
        for i in keyss:
            data = resp[i]
            data =data.json()
            for x in data:
                rtn.append(x)
        return rtn

    def get_campus_cursus_users(self, campus_id: int, cursus_id : int) -> list:
        "GET /v2/cursus/:cursus_id/cursus_users"
        params = {
            "filter[campus_id]": campus_id,        
        }
        resp = self.__api.Api.page("/v2/cursus/{}/cursus_users".format(cursus_id), params=params)
        keyss = resp.keys()
        cursus_data = []
        for i in keyss:
            data = resp[i]
            data = data.json()
            for x in data:
                cursus_data.append(x)
        return cursus_data
    

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")