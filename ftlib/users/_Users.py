import requests
from ..exceptions._Exceptions import UserIdNotFound

__all__ = ("Users", "User")

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")

class User:
    def __init__(self, data : dict, ftlib) -> None:
        self.data = data
        self.__ftlib = ftlib

    def add_correction(self, reason: str,amount : int = 1):
        """
            Adds correction point to self login.
            ARGS:
                reason (str) : reason,
                amount (int) : amount. default is 1
        """
        self.__ftlib.tokener()
        resp = requests.post(f"{self.__ftlib.endpoint}/v2/users/{self.login}/correction_points/add", headers=self.__ftlib.header, data={"amount":amount, "reason":reason})
        self.__ftlib.eval_resp(resp)

    def del_correction(self, reason:str, amount : int = 1):
        """
            Deletes correction point from self login.
            ARGS:
                reason (str) : reason,
                amount (int) : amount. default is 1
        """
        self.__ftlib.tokener()
        resp = requests.delete(f"{self.__ftlib.endpoint}/v2/users/{self.login}/correction_points/remove", headers=self.__ftlib.header, data={"amount":amount, "reason":reason})
        self.__ftlib.eval_resp(resp)

    
    def get_candidate_data(self) -> dict:
        """
            Returns candidature data of self User
            RETURNS:
                dict: data 
        """
        #"/v2/users/:user_id/user_candidature"
        self.__ftlib.tokener()
        resp = requests.get(f"{self.__ftlib.endpoint}/v2/users/{self.login}/user_candidature", headers=self.__ftlib.header)
        self.__ftlib.eval_resp(resp)
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
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib

    def get_user_by_login(self, login : str):
        """
            Returns User object by given login.
            ARGS:
                login: user login,
            RETURN:
                User: User object
        """
        params = {"filter[login]": login, "filter[primary_campus_id]": self.__ftlib.campus_id}
        resp : dict = self.__ftlib.Api.page("/v2/users", params=params)
        keys = resp.keys()
        for i in keys:
            lst = resp[i].json()
            for k in lst:
                if k["login"] == login:
                    return User(k, self.__ftlib)
        raise UserIdNotFound
    
    def get_users_by_logins(self, login_list : list) -> list:
        """
            Returns list of User object.
            RETURN:
                list: List of User object
        """
        rtn = []
        params = {}
        params["filter[primary_campus_id]"] = self.__ftlib.campus_id
        that_users = ""
        for i in login_list:
            that_users += "," + str(i)
        params["filter[login]"] = that_users
        data = self.__ftlib.Api.page("/v2/campus/{}/users".format(self.__ftlib.campus_id), params=params)
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data
    
    
    def get_campus_users(self, campus_id : int):
        """
            Returns campus users of setted campus_id.
            RETURN:
                list: list of users
        """
        to = "/v2/cursus/:cursus_id/cursus_users"
        param = {
            "filter[campus_id]":self.__ftlib.campus_id
        }
        #resp : list = self.__ftlib.s_request(requests.get, f"{self.__ftlib.endpoint}/v2/campus/{self.__ftlib.campus_id}/users", headers=self.__ftlib.header)
        data = self.__ftlib.Api.page("/v2/campus/{}/users".format(campus_id))
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data

    def location_stats(self, login : str, begin_at : str = None, end_at : str = None):
        data = {}
        if (begin_at):
            data["begin_at"] = begin_at
        if (end_at):
            data["end_at"] = end_at
        return self.__ftlib.Api.get("/v2/users/{}/locations_stats".format(login), data=data).json()

