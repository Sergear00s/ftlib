




class Candidatures:
    def __init__(self, api) -> None:
        self.__api = api
    

    def get_user_candidature(self, login : str) -> dict:
        """GET /v2/users/:user_id/user_candidature"""
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

