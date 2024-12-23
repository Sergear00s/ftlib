

class Quest:
    def __init__(self, api) -> None:
        self.__api = api
    
    def get_user_quests(self, user_id : str):
        """GET /v2/users/:user_id/quests"""

        data = self.__api.Api.page("/v2/users/{}/quests".format(user_id))
        data = self.__api.format_page_resp(data)
        return data
    
    def get_campus_users_quests(self, campus_id : int):
         """/v2/campus/:campus_id/quests"""

         data = self.__api.Api.page("/v2/quests", params={"filter[campus_id]":campus_id})
         data = self.__api.format_page_resp(data)
         return data