

class Achivement:
    def __init__(self, root) -> None:
        self.__api = root



    def achive(self, user_id : str, achivement_id : int):
        """POST /v2/achievements_users"""
        self.__api.Api.post("/v2/achievements_users", json={"achivement_id": achivement_id, "user_id":user_id})
        return