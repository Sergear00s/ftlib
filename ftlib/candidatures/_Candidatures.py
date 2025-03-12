from ..credentials import Credentials
from ..api import Api
from ..data import CandidateData
from ..users import Users

class Candidatures:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def get_user_candidature(self, login : str) -> CandidateData:
        """
            login : str
            returns: user candidature data
            description: Get user candidature
        """
        data = self.__api.get("/v2/users/{}/user_candidature".format(login)).json()
        return CandidateData(data)

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
    campus_id: int = None) -> list[CandidateData]:
        args = {key: value for key, value in locals().items() if key != "self" and value is not None}
        keyss = args.keys()
        param = {}
        for i in keyss:
            new_key = "filter[{}]".format(i)
            new_val = args[i]
            param[new_key] = new_val
        data = self.__api.page("/v2/user_candidatures", params=param)
        for i in range(len(data)):
            data[i] = CandidateData(data[i])
        return data


    def get_user_candidatures_by_login_list(self, login_list: list, campus_id : int) -> list[CandidateData]:
        """
            user_ids : list
            returns: list of user candidatures
            description: Get user candidatures by user list
        """
        id_list = []
        userobj = Users(self.__api._credentials)
        user = userobj.get_users_by_logins(login_list, campus_id)
        for i in user:
            id_list.append(str(i.id))
        raw =", ".join(id_list)
        return self.get_user_candidatures(user_id=raw, campus_id = campus_id)