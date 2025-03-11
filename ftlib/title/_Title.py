from ..api import Api
from ..credentials import Credentials


class Title:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)
    
    def set_user_title(self, user_id : str, title_id : str):
        """/v2/titles_users"""
        resp = self.__api.post("/v2/titles_users", json={"user_id":user_id, "title_id" : title_id})

    def get_titles(self):
        """/v2/titles"""
        data = self.__api.page("/v2/titles")
        return data