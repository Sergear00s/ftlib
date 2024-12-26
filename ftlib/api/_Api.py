import requests
from ..exceptions._Exceptions import RateLimit
import time
from concurrent.futures import ThreadPoolExecutor
import copy

class Api:
    def __init__(self, root) -> None:
        self.__api = root

    def _request(self, method : str, endpoint : str, **kwargs):
        self.__api.tokener()
        header = self.__api.header
        url = self.__api.endpoint + endpoint
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        for i in header.keys():
            kwargs["headers"][i] = header[i]
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
        number_page = 1
        page_size = 100
        pages = {}
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        if "params" not in kwargs:
            kwargs["params"] = {}
        kwargs["params"]["page[size]"] = str(page_size)
        kwargs["params"]["page[number]"] = "1"
        resp = self._request("get", endpoint, **kwargs)
        self.__api.eval_resp(resp)
        pages[0] = resp
        x_total = int(resp.headers.get("x-total"))
        if (x_total <= page_size):
            return pages
        number_page = (x_total // page_size) + 1
        i = 2
        resp = None
        base = kwargs.copy()
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = []
            while i <= number_page + 1:
                args = copy.deepcopy(base)
                args["params"]["page[number]"] = str(i)
                args["params"]["page[size]"] = str(page_size)
                futures.append(executor.submit(self.pages_thread, endpoint, **args))
                i += 1 
            i = 1
            for x in futures:
                pages[i] = x.result()
                i += 1
        return pages
    
    def pages_thread(self, endpoint, **kwargs):
        for i in range(20):
            try:
                resp = self._request("get", endpoint, **kwargs)
                self.__api.eval_resp(resp)
                return resp
            except RateLimit as e:
                time.sleep(2)
                continue
            except Exception as e:
                raise e
        raise RuntimeError("Thread Didnt work")