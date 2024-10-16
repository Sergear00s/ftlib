
class Journal():
    def __init__(self, api) -> None:
        self.__api = api
    
    def journal(self,begin_at:str, end_at:str, login : str, keys : dict = None):
        user_id = self.__api.Users.get_user_id_by_login(login)
        if user_id == 0:
            raise Exception("Users.get_user_id_by_login is returned 0")
        params = {
                "filter[user_id]" : user_id,
            }
        data = {"begin_at": begin_at, "end_at": end_at}
        lst = keys.keys()
        for i in lst:
            params[i] = keys[i]
        pages = self.__api.page_request(self.__api.endpoint + f"/v2/campus/{self.__api.campus_id}/journals", headers=self.__api.header, params=params, data=data)
        rtn = []
        for i in pages:
            for x in i:
                rtn.append(x)
        return rtn
    
    def get_evo(self, login:str, begin_at:str, end_at:str):
        return self.journal(begin_at=begin_at, end_at=end_at, login=login, keys={"filter[item_type]":"ScaleTeam"})
    
    def get_intra_usage(self, login:str, begin_at:str, end_at:str):
        return self.journal(begin_at=begin_at, end_at=end_at, login=login, keys={"filter[item_type]":"User"})
    
    def get_interns(self, login:str, begin_at:str, end_at:str):
        return self.journal(begin_at=begin_at, end_at=end_at, login=login, keys={"filter[item_type]":"Internship"})
    
    