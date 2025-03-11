import requests

class Journal():
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib
    
    def __journal(self, campus_id : int ,begin_at:str, end_at:str, keys : dict = None):
        data = {"begin_at": begin_at, "end_at": end_at}
        params = {}
        lst = keys.keys()
        for i in lst:
            params[i] = keys[i]
        data = self.__ftlib.Api.page("/v2/campus/{}/journals".format(campus_id), params=params, data=data)
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data
    
    def get_evo(self, campus_id : int, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(campus_id, begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"ScaleTeam",  "filter[user_id]" :self.__ftlib.Users.get_user_by_login(login)}.id)
    
    def get_intra_usage(self, campus_id : int, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(campus_id, begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"User",  "filter[user_id]" : self.__ftlib.Users.get_user_by_login(login).id})
    
    def get_interns(self, campus_id : int, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(campus_id, begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"Internship",  "filter[user_id]" :self.__ftlib.Users.get_user_by_login(login).id})

    def get_xp(self, campus_id : int, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(campus_id, begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"Experiance",  "filter[user_id]" :self.__ftlib.Users.get_user_by_login(login).id})
    
    def __gather(self, ids, lst):
        rtn = []
        for i in lst:
            if i["user_id"] == ids:
                rtn.append(i)
        return rtn

    def get_list(self, campus_id : int, logins:list, begin_at:str, end_at:str, intern=False, intra_usage=False, evaluation=False, experience=False, location=False) -> dict:
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
        param["filter[campus_id]"] = self.__ftlib.campus_id
        users = []
        line_ids = ""
        for i in logins:
            user = self.__ftlib.Users.get_user_by_login(i)
            line_ids += "," + str(user.id)
            users.append(user)
        param["filter[user_id]"] = line_ids
        lst = self.__journal(campus_id, begin_at, end_at, param)
        rtn = {}
        for i in users:
            rtn[i.login] = self.__gather(i.id, lst)
        return rtn

__all__ = ["Journal"]
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")