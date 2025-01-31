

class Achivement:
    def __init__(self, root) -> None:
        self.__api = root

    def get_campus_achievements(self, campus_id : int):
        """
            campus_id : int
            returns: list of campus achivements
            description: Get all achivements of a campus
        """
        data = self.__api.Api.page("/v2/campus/{}/achievements".format(campus_id))
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data
        
    def achieve(self, user_id : str, achivement_id : int):
        """
            user_id : str
            achivement_id : int
            description: Give an achivement to a user
        """
        resp = self.__api.Api.post("/v2/achievements_users", json={"achievement_id": achivement_id, "user_id":user_id})