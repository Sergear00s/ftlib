




class Candidatures:
    def __init__(self, api) -> None:
        self.__api = api
    

    def get_user_candidature(self, login : str) -> dict:
        """
            login : str
            returns: user candidature data
            description: Get user candidature
        """
        return self.__api.Api.get("/v2/users/{}/user_candidature".format(login))

    def get_user_candidatures(
    self, 
    id: int = None,
    user_id: int = None,
    birth_date: str = None,
    gender: str = None,
    country: str = None,
    birth_country: str = None,
    postal_country: str = None,
    piscine_date: str = None,
    email: str = None, 
    campus_id: int = None):
        args = {key: value for key, value in locals().items() if key != "self" and value is not None}
        keyss = args.keys()
        param = {}
        for i in keyss:
            new_key = "filter[{}]".format(i)
            new_val = args[i]
            param[new_key] = new_val
        data = self.__api.Api.page("/v2/user_candidatures", params=param)
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data


    def get_user_candidatures_by_user_list(self, user_ids: list):
        """
            user_ids : list
            returns: list of user candidatures
            description: Get user candidatures by user list
        """
        raw =", ".join(user_ids)
        return self.get_user_candidatures(user_id=raw, campus_id=49)