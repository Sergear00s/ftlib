import requests
from ..exceptions._Exceptions import RateLimit
import time
from concurrent.futures import ThreadPoolExecutor
import copy
from ..exceptions._Exceptions import Error_response, Error_auth, RateLimit
from ..credentials import Credentials

class Api:
    def __init__(self, credentials : Credentials) -> None:
        self._credentials = credentials

    def _request(self, method : str, endpoint : str, **kwargs):
        self._credentials.tokener()
        header = self._credentials.header
        url = self._credentials.endpoint + endpoint
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        for i in header.keys():
            kwargs["headers"][i] = header[i]
        resp = requests.request(method, url, **kwargs)
        self.__eval_resp(resp)
        return resp

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
    
    def page(self, endpoint, **kwargs) -> list:
        """
            endpoint : str
            description: Get all pages of a endpoint
            format: {page_number: requests.Response() , ...}                
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
        self.__eval_resp(resp)
        pages[0] = resp
        x_total = int(resp.headers.get("x-total"))
        if (x_total <= page_size):
            data = self.__format_page_resp(pages)
            data = self.__extract(data)
            return data
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
                futures.append(executor.submit(self.__pages_thread, endpoint, **args))
                i += 1 
            i = 1
            for x in futures:
                pages[i] = x.result()
                i += 1
        data = self.__format_page_resp(pages)
        data = self.__extract(data)
        return data
    
    def __pages_thread(self, endpoint, **kwargs):
        for i in range(20):
            try:
                resp = self._request("get", endpoint, **kwargs)
                #self._credentials.eval_resp(resp)
                return resp
            except RateLimit as e:
                time.sleep(2)
                continue
            except Exception as e:
                raise e
        raise RuntimeError("Thread Didnt work")
    
    #"""formatting page"""#

    def __eval_resp(self, response):
        codes = [500, 400, 429, 401, 403, 404, 422]
        if (response.status_code == codes[0]):
            raise Error_response(f'{response, response.json()}')
        if (response.status_code == codes[1]):
            raise Error_auth(f'{response, response.json()}')
        if (response.status_code == codes[2]):
            raise RateLimit("RateLimit")
        if (response.status_code == codes[3]):
            raise Error_auth(f'{response, response.json()}')
        if (response.status_code in codes):
            raise Exception(f'{response, response.json()}')

    def __format_page_resp(self, data : dict) -> dict:
        keyss = data.keys()
        for i in keyss:
            val = data[i].json()
            data[i] = val
        return data

    def __extract(self, data : dict) -> list:
        keys = data.keys()
        rtn = []
        for i in keys:
            data_in = data[i]
            for x in data_in:
                rtn.append(x)
        return rtn

