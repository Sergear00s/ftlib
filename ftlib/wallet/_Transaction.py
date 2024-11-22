


import requests

class Transaction:
    def __init__(self, api) -> None:
        self.__api = api


    def send(self, user_id : str, amount : int, reason : str, transactable_type : str = "Tuteur api"):
        
        if (amount <= 0):
            raise ArithmeticError("amount can't be negative or null")
        data = {
            "value": amount,
            "user_id": user_id,
            "transactable_type": transactable_type,
            "reason": reason
        }

        resp = self.__api.api.post("/v2/transactions", data=data)
        self.__api.eval_resp(resp)


    def recive(self, user : str, amount : int):
        pass

    def trade(self, from_ : str, to_ : str, amount : int):
        pass

    def get_transactions(self, campus_id : int, created_at : str):
        pass


        