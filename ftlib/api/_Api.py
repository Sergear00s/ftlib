import requests



class Api:
    def __init__(self, root) -> None:
        self.__api = root

    def get(self, endpoint, params=None, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        return requests.request("get", url, params=params, headers=header, **kwargs)
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        return requests.request("post", url, headers=header, data=data, json=json, **kwargs)
    
    def put(self, endpoint, data=None, json=None, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        return requests.request("put", url, data=data, headers=header, json=json, **kwargs)
    

    def patch(self, endpoint, data=None, json=None, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        return requests.request("patch", url, data=data, headers=header, json=json, **kwargs)
    

    def delete(self, endpoint, data=None, json=None, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        return requests.request("delete", url, data=data, headers=header, json=json, **kwargs)
    
