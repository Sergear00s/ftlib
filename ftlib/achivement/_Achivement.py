from ..api import Api
from ..credentials import Credentials

class Achivement:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def get_campus_achievements(self, campus_id : int):
        """
            campus_id : int
            returns: list of campus achivements
            description: Get all achivements of a campus
        """
        data = self.__api.page("/v2/campus/{}/achievements".format(campus_id))
        for i in range(len(data)):
            data[i] = AchivementData(data[i])
        return data
        
    def achieve(self, user_id : str, achivement_id : int):
        """
            user_id : str
            achivement_id : int
            description: Give an achivement to a user
        """
        resp = self.__api.post("/v2/achievements_users", json={"achievement_id": achivement_id, "user_id":user_id})