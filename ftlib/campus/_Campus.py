

class Campus:
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib
    

    def get_all_campuses(self):
        """
            returns: list of campuses
            description: Get all campuses
        """
        data = self.__ftlib.format_page_resp(self.__ftlib.Api.page("/v2/campus"))
        data = self.__ftlib.extract(data)
        return data