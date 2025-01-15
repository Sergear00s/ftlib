


class Title:
    def __init__(self, root) -> None:
        self.__api = root
    
    def set_user_title(self, user_id : str, title_id : str):
        """/v2/titles_users"""
        resp = self.__api.Api.post("/v2/titles_users", json={"user_id":user_id, "title_id" : title_id})

    def get_titles(self):
        """/v2/titles"""
        data = self.__api.Api.page("/v2/titles")
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data