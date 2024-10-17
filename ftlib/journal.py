
class Journal():
    def __init__(self, api) -> None:
        self.__api = api
    
    def __journal(self,begin_at:str, end_at:str, keys : dict = None):
        data = {"begin_at": begin_at, "end_at": end_at}
        params = {}
        lst = keys.keys()
        for i in lst:
            params[i] = keys[i]
        pages = self.__api.s_request(self.__api.endpoint + f"/v2/campus/{self.__api.campus_id}/journals", headers=self.__api.header, params=params, data=data)
        rtn = []
        for i in pages:
            for x in i:
                rtn.append(x)
        return rtn

    # def journal(self,begin_at:str, end_at:str, login : str, keys : dict = None):
    #     user_id = self.__api.Users.get_user_id_by_login(login)
    #     if user_id == 0:
    #         raise Exception("Users.get_user_id_by_login is returned 0")
    #     params = {
    #             "filter[user_id]" : user_id,
    #         }
    #     data = {"begin_at": begin_at, "end_at": end_at}
    #     lst = keys.keys()
    #     for i in lst:
    #         params[i] = keys[i]
    #     pages = self.__api.s_request(self.__api.endpoint + f"/v2/campus/{self.__api.campus_id}/journals", headers=self.__api.header, params=params, data=data)
    #     rtn = []
    #     for i in pages:
    #         for x in i:
    #             rtn.append(x)
    #     return rtn
    
    def get_evo(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        ids = self.__api.Users.get_user_id_by_login(login)
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"ScaleTeam",  "filter[user_id]" :ids})
    
    def get_intra_usage(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        ids = self.__api.Users.get_user_id_by_login(login)
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"User",  "filter[user_id]" :ids})
    
    def get_interns(self, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        ids = self.__api.Users.get_user_id_by_login(login)
        return self.__journal(begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"Internship",  "filter[user_id]" :ids})
    

    def __gather(ids, lst):
        rtn = []
        for i in lst:
            if i["user_id"] == ids:
                rtn.append(i)
        return rtn



    def get_list(self, logins:list, begin_at:str, end_at:str, intern=False, intra_usage=False, evaluation=False):
        keys = []
        if (intern):
            keys.append("Internship")
        if (intra_usage):
            keys.append("User")
        if (evaluation):
            keys.append("ScaleTeam")
        param = {}
        if (len(keys) == 3):
            param["filter[item_type]"] = keys[0] + "," + keys[1] + "," + keys[2]
        if (len(keys) == 2):
            param["filter[item_type]"] = keys[0] + "," + keys[1]
        if (len(keys) == 1):
            param["filter[item_type]"] = keys[0]
        param["filter[campus_id]"] = self.__api.campus_id
        lst = self.__journal(begin_at, end_at, param)
        id_list = []
        for l in logins:
            ids = self.__api.Users.get_user_id_by_login(l)
            id_list.append((l, ids))
        rtn = {}
        for i in id_list:
            rtn[i[0]] = self.__gather(i[1], lst)
        return rtn
