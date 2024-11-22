


import requests
import datetime


class Transaction:
    def __init__(self, api) -> None:
        self.__api = api


    def send(self, user_id : str, amount : int, transactable_type : str = "Tuteur api"):
        """"transaction": {
    "value": 5,
    "user_id": 123,
    "transactable_type": "Tuteur api",
    "reason": "cadeau"
    /v2/transactions
  }"""
        
        if (amount <= 0):
            raise ArithmeticError("amount can't be negative or null")
        data = {
            "transaction" : {
                "value" : str(amount),
                "user_id": user_id,
                "transactable_type": transactable_type
            }
        }
        resp = self.__api.api.post("/v2/transactions", headers=self.__api.header, data=data)
        self.__api.eval_resp(resp)


    def recive(self, user : str, amount : int):
        pass

    def trade(self, from_ : str, to_ : str, amount : int):
        pass

    def get_transactions(self, campus_id : int, created_at : str):
        pass


        