import datetime
from ..api import Api
from ..credentials import Credentials
from ..data import ExamData

class Exam:
    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def create_exam(self, name:str, begin_at : datetime.datetime, end_at: datetime.datetime, location:str, ip_range:str, campus_id:int, project_ids : list, visible : bool = True, max_people : int = None,  activate_waitlist : bool = False):
        """
            name : str
            begin_at : datetime.datetime
            end_at : datetime.datetime
            location : str
            ip_range : str
            campus_id : int
            project_ids : list
            visible : bool
            max_people : int
            activate_waitlist : bool
            description: Create an exam
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
        data = self.__api.post("/v2/exams", json={"exam": params})

    def get_exams(self, campus_id : int, before_days : int = None) -> list[ExamData]:
        """
            campus_id : int
            returns: list of exams of a campus
        """
        params = {}
        if (before_days):
            delta = datetime.timedelta(days=before_days)
            params["range[begin_at]"] = (datetime.datetime.now() - delta).isoformat(timespec='milliseconds') + 'Z' + "," + datetime.datetime.now().isoformat(timespec='milliseconds') + 'Z'
        data = self.__api.page("/v2/campus/{}/exams".format(campus_id), params=params)
        for i in range(len(data)):
            data[i] = ExamData(data[i])
        return data

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
        """
            exam_id : int
            name : str
            begin_at : datetime.datetime
            end_at : datetime.datetime
            location : str
            ip_range : str
            campus_id : int
            project_ids : list
            visible : bool
            max_people : int
            activate_waitlist : bool
            description: Update an exam
        """
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
        data = self.__api.put("/v2/exams/{}".format(exam_id), json={"exam": data})
        return data

    def delete_exam(self, exam_id : int):
        """
            exam_id : int
            description: Delete an exam
        """
        data = self.__api.delete("/v2/exams/{}".format(exam_id))
        return data
        
    def get_exam_users_by_exam_id(self, exam_id : int):
        """
            exam_id : int
            returns: list of exam users
            description: Get exam users by exam id
        """
        params = {}
        params["filter[exam_id]"] = exam_id
        data = self.__api.page("/v2/exams/{}/exams_users".format(exam_id), params=params)
        return data
    
    def upload_exam_users(self, user_id_list : list, exam_id : int):
        """
            user_id_list : list
            exam_id : int
            description: Upload exam users
        """
        users = self.__ftlib.Users.get_users_by_logins(user_id_list)
        ids = []
        for x in users:
            ids.append(str(x["id"]))
        raw = ", ".join(ids)
        param = {}
        param["exams_user[user_id]"] = raw
        data = self.__api.post("/v2/exams/{}/exams_users".format(exam_id), params=param)
        return data
    def delete_exam_user(self, exam_id : int, user_id : str):
        """
            exam_id : int
            user_id : str
            description: Delete an exam user
        """
        data = self.__api.post("/v2/exams/{}/exams_users/{}".format(exam_id, user_id))

