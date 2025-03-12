from ..api import Api
from ..credentials import Credentials
from ..data import JournalData

##todo

class Journal():
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)
    
    def __journal(self, campus_id : int ,begin_at:str, end_at:str, keys : dict = None):
        data = {"begin_at": begin_at, "end_at": end_at}
        params = {}
        lst = keys.keys()
        for i in lst:
            params[i] = keys[i]
        data = self.__api.page("/v2/campus/{}/journals".format(campus_id), params=params, data=data)
        for i in range(len(data)):
            data[i] = JournalData(data)
        return data
    
    def get_evo(self, campus_id : int, login:str, begin_at:str, end_at:str):
        """
            login: username,
            begin_at: "yyy-mm-dd",
            end_at: "yyy-mm-dd"
        """
        return self.__journal(campus_id, begin_at=begin_at, end_at=end_at, keys={"filter[item_type]":"ScaleTeam",  "filter[user_id]" :self.__ftlib.Users.get_user_by_login(login).id})
    
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
    
