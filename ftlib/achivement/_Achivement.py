

class Achivement:
    def __init__(self, root) -> None:
        self.__api = root



    def achieve(self, user_id : str, achivement_id : int):
        """POST /v2/achievements_users"""
        resp = self.__api.Api.post("/v2/achievements_users", json={"achievement_id": achivement_id, "user_id":user_id})
        return resp