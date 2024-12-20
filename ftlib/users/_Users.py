import requests
from ..exceptions._Exceptions import UserIdNotFound

__all__ = ("Users", "User")

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")

class User:
    def __init__(self, data : dict, api) -> None:
        self.data = data
        self.__api = api

    def add_correction(self, reason: str,amount : int = 1):
        """
            Adds correction point to self login.
            ARGS:
                reason (str) : reason,
                amount (int) : amount. default is 1
        """
        self.__api.tokener()
        resp = requests.post(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/add", headers=self.__api.header, data={"amount":amount, "reason":reason})
        self.__api.eval_resp(resp)

    def del_correction(self, reason:str, amount : int = 1):
        """
            Deletes correction point from self login.
            ARGS:
                reason (str) : reason,
                amount (int) : amount. default is 1
        """
        self.__api.tokener()
        resp = requests.delete(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/remove", headers=self.__api.header, data={"amount":amount, "reason":reason})
        self.__api.eval_resp(resp)

    
    def get_candidate_data(self) -> dict:
        """
            Returns candidature data of self User
            RETURNS:
                dict: data 
        """
        #"/v2/users/:user_id/user_candidature"
        self.__api.tokener()
        resp = requests.get(f"{self.__api.endpoint}/v2/users/{self.login}/user_candidature", headers=self.__api.header)
        self.__api.eval_resp(resp)
        return resp.json()

    def __getattr__(self, name):
        """['id', 'email', 'login', 'first_name', 'last_name', 'usual_full_name', 'usual_first_name', 'url', 'phone', 'displayname', 'kind', 'image', 'staff?', 'correction_point', 'pool_month', 'pool_year', 'location', 'wallet', 'anonymize_date', 'data_erasure_date', 'created_at', 'updated_at', 'alumnized_at', 'alumni?', 'active?']"""
        if name in self.data:
            return self.data[name]
        raise AttributeError(f"'User' object has no attribute '{name}'")
    
    def __str__(self) -> str:
        try:
            login = self.data
            return str(login)
        except:
            return ""
    def __repr__(self) -> str:
        return str(self.data)


class Users:
    def __init__(self, api) -> None:
        self.__api = api

    def get_user_by_login(self, login : str):
        """
            Returns User object by given login.
            ARGS:
                login: user login,
            RETURN:
                User: User object
        """
        params = {"filter[login]": login, "filter[primary_campus_id]": self.__api.campus_id}
        resp : dict = self.__api.Api.page("/v2/users", params=params)
        keys = resp.keys()
        for i in keys:
            lst = resp[i].json()
            for k in lst:
                if k["login"] == login:
                    return User(k, self.__api)
        raise UserIdNotFound
    
    def get_users_by_logins(self, login_list : list) -> list:
        """
            Returns list of User object.
            RETURN:
                list: List of User object
        """
        rtn = []
        params = {}
        params["filter[primary_campus_id]"] = self.__api.campus_id
        that_users = ""
        for i in login_list:
            that_users += "," + str(i)
        params["filter[login]"] = that_users
        value = self.__api.Api.page("/v2/campus/{}/users".format(self.__api.campus_id), params=params)
        keys = value
        for i in keys:
            data = value[i]
            data = data.json()
            for user in data:
                rtn.append(User(user, self.__api))
        return rtn
    
    
    def get_campus_users(self, campus_id : int):
        """
            Returns campus users of setted campus_id.
            RETURN:
                list: list of users
        """
        to = "/v2/cursus/:cursus_id/cursus_users"
        param = {
            "filter[campus_id]":self.__api.campus_id
        }
        #resp : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/campus/{self.__api.campus_id}/users", headers=self.__api.header)
        resp = self.__api.Api.page("/v2/campus/{}/users".format(campus_id))
        keyss = resp.keys()
        users = []
        for i in keyss:
            data = resp[i]
            data = data.json()
            for x in data:
                users.append(User(x, self.__api))
        return users

    def location_stats(self, login : str, begin_at : str = None, end_at : str = None):
        data = {}
        if (begin_at):
            data["begin_at"] = begin_at
        if (end_at):
            data["end_at"] = end_at
        return self.__api.Api.get("/v2/users/{}/locations_stats".format(login), data=data).json()

