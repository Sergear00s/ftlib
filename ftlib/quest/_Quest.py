

class Quest:
    def __init__(self, api) -> None:
        self.__api = api
    

    def get_user_quests(self, user_id : str):
        """GET /v2/users/:user_id/quests"""

        data = self.__api.Api.page("/v2/users/{}/quests".format(user_id))
        data = self.__api.format_page_resp(data)
        return data
    
    def get_campus_users_quests(self, campus_id : int, quest_id_list : list):
         """/v2/campus/:campus_id/quests"""
         quest_id_list = [str(x) for x in quest_id_list]
         formated = ", ".join(quest_id_list)
         data = self.__api.Api.page("/v2/quests_users", params={"filter[campus_id]":campus_id, "filter[quest_id]": formated})
         data = self.__api.format_page_resp(data)
         return data
    

    def get_users_quests(self, user_list : list, quest_id : int):
        """/v2/quests_users"""
        """/v2/quests/:quest_id/quests_users"""

        user_format = ", ".join(user_list)
        print(user_format)
        data = self.__api.Api.page("/v2/quests/{}/quests_users".format(quest_id), params={"filter[user_id]": user_format})
        data = self.__api.format_page_resp(data)
        return data
