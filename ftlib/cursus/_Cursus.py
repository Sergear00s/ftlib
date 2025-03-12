from ..credentials import Credentials
from ..api import Api
from ..data import CursusUserData
class Cursus:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

        
    def get_user_cursus(self, user_id : str) -> CursusUserData:
        """
            user_id : str
            returns: list of user cursus
            description: Get user cursus
        """
        data : list[CursusUserData] = self.__api.page("/v2/users/{}/cursus_users".format(user_id))

        for i in range(len(data)):
            data[i] = CursusUserData(data[i])
        user = None
        for i in data:
            if i.user.login == user_id:
                user = i
                break
        return user

    def get_campus_cursus_users(self, campus_id: int, cursus_id : int) -> list[CursusUserData]:
        """
            campus_id : int
            cursus_id : int
            returns: list of campus cursus users data
            description: Get campus cursus users data
        """
        params = {
            "filter[campus_id]": campus_id,        
        }
        data = self.__api.page("/v2/cursus/{}/cursus_users".format(cursus_id), params=params)
        for i in range(len(data)):
            data[i] = CursusUserData(data[i])
        return data
    
