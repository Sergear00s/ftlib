import requests


class Journal():
    def __init__(self, api) -> None:
        self.__api = api
    
    def __journal(self,begin_at:str, end_at:str, keys : dict = None):
        data = {"begin_at": begin_at, "end_at": end_at}
        params = {}
        lst = keys.keys()
        for i in lst:
            params[i] = keys[i]
        pages = self.__api.s_request(requests.get, self.__api.endpoint + f"/v2/campus/{self.__api.campus_id}/journals", headers=self.__api.header, params=params, data=data)
        rtn = []
        for i in pages:
            for x in i:
                rtn.append(x)
        return rtn

    
    def get_evo(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"ScaleTeam",  "filter[user_id]" :self.__api.Users.get_user_by_login(login)}.id)
    
    def get_intra_usage(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"User",  "filter[user_id]" : self.__api.Users.get_user_by_login(login).id})
    
    def get_interns(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"Internship",  "filter[user_id]" :self.__api.Users.get_user_by_login(login).id})

    def get_xp(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"Experiance",  "filter[user_id]" :self.__api.Users.get_user_by_login(login).id})
    

    def __gather(self, ids, lst):
        rtn = []
        for i in lst:
            if i["user_id"] == ids:
                rtn.append(i)
        return rtn


    def get_list(self, logins:list, begin_at:str, end_at:str, intern=False, intra_usage=False, evaluation=False, experience=False, location=False) -> dict:
        """
            logins : list of users
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
            return type: dict
        """
        keys = []
        if (intern):
            keys.append("Internship")
        if (intra_usage):
            keys.append("User")
        if (evaluation):
            keys.append("ScaleTeam")
        if (experience):
            keys.append("Experience")
        if (location):
            keys.append("Location")
        param = {}
        if (len(keys)):
            param["filter[item_type]"] = ",".join(keys)
        else:
            param["filter[item_type]"] = "Internship,User,ScaleTeam,Experience"
        param["filter[campus_id]"] = self.__api.campus_id
        users = []
        line_ids = ""
        for i in logins:
            user = self.__api.Users.get_user_by_login(i)
            line_ids += "," + str(user.id)
            users.append(user)
        param["filter[user_id]"] = line_ids
        lst = self.__journal(begin_at, end_at, param)
        rtn = {}
        for i in users:
            rtn[i.login] = self.__gather(i.id, lst)
        return rtn



__all__ = ["Journal"]
