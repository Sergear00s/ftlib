from ..credentials import Credentials
from ..api import Api
from ..data import CampusData

class Campus:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def get_all_campuses(self) -> list[CampusData]:
        """
            returns: list of campuses
            description: Get all campuses
        """
        data = self.__api.page("/v2/campus")
        for i in range(len(data)):
            data[i] = CampusData(data[i])
        return data