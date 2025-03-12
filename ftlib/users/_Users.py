from ..exceptions._Exceptions import UserIdNotFound
from ..api import Api
from ..credentials import Credentials
from ..data import *



class Users:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def get_user_by_login(self, login : str, campus_id : int) -> UserData:
        """
            Returns User object by given login.
            ARGS:
                login: user login,
                campus_id: campus id
            RETURN:
                User: User data dict
        """
        params = {"filter[login]": login, "filter[primary_campus_id]": campus_id}
        resp = self.__api.page("/v2/users", params=params)
        if len(resp) == 0:
            raise UserIdNotFound("User not found.")
        if resp[0]["login"] != login:
            raise UserIdNotFound("User not found.")
        user = UserData(resp[0])
        return user
    
    def get_users_by_logins(self, login_list : list, campus_id : int) -> list[UserData]:
        """
            Returns list of User object.
            RETURN:
                list: List of User object
        """
        params = {}
        params["filter[primary_campus_id]"] = campus_id 
        that_users = ""
        for i in login_list:
            that_users += "," + str(i)
        params["filter[login]"] = that_users
        data = self.__api.page("/v2/campus/{}/users".format(campus_id), params=params)
        for i in range(len(data)):
            data[i] = UserData(data[i])
        return data
    
    def get_campus_users(self, campus_id : int):
        """
            Returns campus users of setted campus_id.
            RETURN:
                list: list of users
        """
        data = self.__api.page("/v2/campus/{}/users".format(campus_id))
        return data

    def location_stats(self, login : str, begin_at : str = None, end_at : str = None):
        data = {}
        if (begin_at):
            data["begin_at"] = begin_at
        if (end_at):
            data["end_at"] = end_at
        return self.__api.get("/v2/users/{}/locations_stats".format(login), data=data).json()

    def add_evaluate_point(self, login : str, reason : str, amount : int = 1):
        self.__api.post("/v2/users/{}/correction_points/add".format(login), data={"amount": amount, "reason": reason})
    
    def remove_evaluate_point(self, login : str, reason : str, amount : int = 1):
        self.__api.delete("/v2/users/{}/correction_points/remove".format(login), data={"amount": amount, "reason": reason})