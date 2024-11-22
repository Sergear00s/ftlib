import requests



class Api:
    def __init__(self, root) -> None:
        self.__api = root

    def _request(self, method : str, endpoint : str, **kwargs):
        self.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        kwargs["headers"]= header
        return requests.request(method, url, **kwargs)

    def get(self, endpoint, **kwargs):
        return self._request("get", endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self._request("post", endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self._request("put", endpoint, **kwargs)
    

    def patch(self, endpoint, **kwargs):
        return self._request("patch", endpoint, **kwargs)
    

    def delete(self, endpoint, **kwargs):
        return self._request("delete", endpoint, **kwargs)
    
