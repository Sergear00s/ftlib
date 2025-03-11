

class Transaction:
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib

    def send(self, user_id : str, amount : int, reason : str, transactable_type : str = "Tuteur api"):
        
        if (amount <= 0):
            raise ArithmeticError("amount can't be negative or null")
        data = {
            "value": amount,
            "user_id": user_id,
            "transactable_type": transactable_type,
            "reason": reason
        }
        resp = self.__ftlib.Api.post("/v2/transactions", json=data)
        self.__ftlib.eval_resp(resp)

    def recive(self, user_id : str, amount : int, reason : str, transactable_type : str = "Tuteur api"):
        
        if (amount <= 0):
            raise ArithmeticError("amount can't be negative or null")
        data = {
            "value": amount * -1,
            "user_id": user_id,
            "transactable_type": transactable_type,
            "reason": reason
        }
        resp = self.__ftlib.api.post("/v2/transactions", json=data)
        self.__ftlib.eval_resp(resp)

    def trade(self, from_ : str, to_ : str, amount : int, reason : str = "swap"):
        self.recive(from_, amount, reason)
        self.send(to_, amount, reason)

    def get_user_transactions(self, user_id : str):
        """GET /v2/users/:user_id/transactions"""
        data = self.__ftlib.Api.page("/v2/users/{}/transactions".format(user_id))
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data

    def get_transactions(self,
                        created_at : str = None,
                        id_ : str = None,
                        user_id : str = None,
                        transactable_id : str = None,
                        transactable_type : str = None,
                        reason : str = None,
                        ) -> dict:
        args = {
            "created_at": created_at,
            "id": id_,
            "user_id": user_id,
            "transactable_id": transactable_id,
            "transactable_type": transactable_type,
            "reason": reason,
        }
        data = {key: value for key, value in args.items() if value is not None}
        keyss = data.keys()
        param = {}
        for i in keyss:
            new_key = "filter[{}]".format(i)
            new_val = data[i]
            param[new_key] = new_val
        data = self.__ftlib.Api.page("/v2/transactions", params=param)
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return data

    def delete_transaction(self, id_ : str):
        self.__ftlib.Api.delete("/v2/transactions/{}".format(id_))