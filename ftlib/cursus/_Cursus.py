import time
import requests
import json

__all__ = ["Cursus"]

class Cursus:
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib
        
    def get_user_cursus(self, user_id : str) -> list:
        """
            user_id : str
            returns: list of user cursus
            description: Get user cursus
        """
        data = self.__ftlib.Api.page("/v2/users/{}/cursus_users".format(user_id))
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data

    def get_campus_cursus_users(self, campus_id: int, cursus_id : int) -> list:
        """
            campus_id : int
            cursus_id : int
            returns: list of campus cursus users data
            description: Get campus cursus users data
        """
        params = {
            "filter[campus_id]": campus_id,        
        }
        data = self.__ftlib.Api.page("/v2/cursus/{}/cursus_users".format(cursus_id), params=params)
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data
    

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")