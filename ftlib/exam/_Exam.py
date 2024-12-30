import datetime

class Exam:
    def __init__(self, api) -> None:
        self.__api = api


    def create_exam(self, name:str, begin_at : datetime.datetime, end_at: datetime.datetime, location:str, ip_range:str, campus_id:int, project_ids : list, visible : bool = True, max_people : int = None,  activate_waitlist : bool = False):
        """
        """
        params = {}
        params["name"] = name
        params["begin_at"] = begin_at.isoformat(timespec='milliseconds') + 'Z'
        params["end_at"] = end_at.isoformat(timespec='milliseconds') + 'Z'
        params["location"] = location
        params["ip_range"] = ip_range
        params["visible"] = visible
        if (max_people):
            params["max_people"] = max_people
        params["campus_id"] = campus_id
        params["activate_waitlist"] = activate_waitlist
        params["project_ids"] = project_ids
        data = self.__api.Api.post("/v2/exams", json={"exam": params})
        self.__api.eval_resp(data)

    def get_exams(self, campus_id : int):
        pass

    def update_exam(self, exam_id: int, name : str = None,
                    begin_at : str = None, 
                    end_at:str = None, 
                    location:str = None, 
                    ip_range:str = None,
                    campus_id:int= None,
                    project_ids : list = None,
                    visible : bool = None, 
                    max_people : int = None,
                    activate_waitlist : bool = None):
        params = {}
        params["name"] = name
        if (begin_at):
            params["begin_at"] = begin_at.isoformat(timespec='milliseconds') + 'Z'
        if (end_at):
            params["end_at"] = end_at.isoformat(timespec='milliseconds') + 'Z'
        params["location"] = location
        params["ip_range"] = ip_range
        params["visible"] = visible
        params["max_people"] = max_people
        params["campus_id"] = campus_id
        params["activate_waitlist"] = activate_waitlist
        params["project_ids"] = project_ids
        keyss = params.keys()
        data = {}
        for i in keyss:
            if (params[i] != None):
                data[i] = params[i] 
        data = self.__api.Api.put("/v2/exams/{}".format(exam_id), json={"exam": data})
        self.__api.eval_resp(data)

    def delete_exam(self, exam_id : int):
        self.__api.Api.delete("/v2/exams/{}".format(exam_id))
        
    def get_exam_users_by_exam_id(self, exam_id : int):
        """GET /v2/exams/:exam_id/exams_users"""
        params = {}
        params["filter[exam_id]"] = exam_id
        data = self.__api.Api.page("/v2/exams/{}/exams_users".format(exam_id), params=params)
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data
    
    def upload_exam_users(self, user_id_list : list, exam_id : int):
        raw = ", ".join(user_id_list)
        param = {}
        param["exams_user[user_id]"] = raw
        data = self.__api.Api.post("/v2/exams/{}/exams_users".format(exam_id), params=param)
        self.__api.eval_resp(data)
    
    def delete_exam_user(self, exam_id : int, user_id : str):
        """ /v2/exams/:exam_id/exams_users/:id"""
        data = self.__api.Api.post("/v2/exams/{}/exams_users/{}".format(exam_id, user_id))
        self.__api.eval_resp(data)

