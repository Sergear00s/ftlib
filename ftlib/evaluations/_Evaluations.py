from ..credentials import Credentials
from ..api import Api

class Evaluations:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)


    def get_evaluations(self, campus_id : int, created_at:str = None, updated_at:str = None):
        params = {"filter[created_at]": created_at, "filter[updated_at]": updated_at, "filter[campus_id]": campus_id}
        if (updated_at == None):
            del params["filter[updated_at]"]
        if (created_at == None):
            del params["filter[created_at]"]
        data = self.__api.page("/v2/evaluations", params=params)
        return data
    
