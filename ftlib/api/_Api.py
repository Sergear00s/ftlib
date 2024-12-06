import requests
from ..exceptions._Exceptions import RateLimit
import time


class Api:
    def __init__(self, root) -> None:
        self.__api = root

    def _request(self, method : str, endpoint : str, **kwargs):
        self.__api.tokener()
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
    
    def page(self, endpoint, **kwargs) -> dict:
        """
            returns resps in dict page by page. Example = {0: resp, 1: resp, 2, resp...}
        """
        pages = {}
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        kwargs["headers"]["page[size]"] = 100
        kwargs["headers"]["page[number]"] = 1
        resp = self._request("get", endpoint, **kwargs)
        self.__api.eval_resp(resp)
        pages[0] = resp
        x_total = int(resp.headers.get("X-Total"))
        if x_total <= 1:
            return pages
        i = 1
        resp = None
        while (i <= x_total):
            kwargs["headers"]["page[number]"] = i
            for j in range(10):
                resp = None
                resp = self._request("get", endpoint, **kwargs)
                try:
                    self.__api.eval_resp(resp)
                    break
                except RateLimit as e:
                    time.sleep(1)
            if resp == None:
                raise RateLimit(resp)
            pages[i] = resp
            i += 1
        return pages
    
    def pages(self, pagenumber : int, endpoint, **kwargs):
        pass