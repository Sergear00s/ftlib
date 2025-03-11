from ..credentials import Credentials
from ..api import Api

class Cursus:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

        
    def get_user_cursus(self, user_id : str) -> list:
        """
            user_id : str
            returns: list of user cursus
            description: Get user cursus
        """
        data = self.__api.page("/v2/users/{}/cursus_users".format(user_id))
        return data

    def get_campus_cursus_users(self, campus_id: int, cursus_id : int) -> list:
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
        return data
    
