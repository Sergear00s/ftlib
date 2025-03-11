


class Title:
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib
    
    def set_user_title(self, user_id : str, title_id : str):
        """/v2/titles_users"""
        resp = self.__ftlib.Api.post("/v2/titles_users", json={"user_id":user_id, "title_id" : title_id})

    def get_titles(self):
        """/v2/titles"""
        data = self.__ftlib.Api.page("/v2/titles")
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data