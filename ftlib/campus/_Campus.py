

class Campus:
    def __init__(self, api) -> None:
        self.__api = api
    

    def get_all_campuses(self):
        """
            returns: list of campuses
            description: Get all campuses
        """
        data = self.__api.format_page_resp(self.__api.Api.page("/v2/campus"))
        data = self.__api.extract(data)
        return data