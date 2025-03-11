from ..credentials import Credentials
from ..api import Api

class Campus:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def get_all_campuses(self):
        """
            returns: list of campuses
            description: Get all campuses
        """
        data = self.__api.page("/v2/campus")
        return data