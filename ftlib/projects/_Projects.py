from ..api import Api
from ..credentials import Credentials
from ..data import ProjectData

class Projects():

    def __init__(self, credentials : Credentials) -> None:
        self.__api = Api(credentials)

    def update_project_mark(self, project_id : int, final_mark : int) -> None:
        """
            project_id : int
            final_mark : int
            description: Update project mark
        """
        data = self.__api.patch("/v2/projects_users/{}".format(project_id), json={"projects_user": {"final_mark": final_mark}})
        return data
    #todo: 
    def delete_evaluate(self):
        pass

    def get_projects(self, cursus_id : int):
        """
            cursus_id : int
            returns: list of projects of a cursus
        """
        data = self.__api.page("/v2/cursus/{}/projects".format(cursus_id))
        for i in range(len(data)):
            data[i] = ProjectData(data[i])
        return data
    
    def get_projects_by_list(self, project_ids : list, cursus_id):
        """
            project_ids : list
            cursus_id : int
            returns: list of projects of a cursus
        """
        project_ids_ = ", ".join(project_ids)
        data = self.__api.page("/v2/cursus/{}/projects".format(cursus_id), params={"filter[id]": project_ids_})
        for i in range(len(data)):
            data[i] = ProjectData(data[i])
        return data
    def get_project(self, project_id : int, cursus_id : int) -> ProjectData:
        """
            project_id : int
            cursus_id : int
            returns: project data of a cursus by project id
        """
        data = self.__api.page("/v2/cursus/{}/projects".format(cursus_id), params={"filter[id]": project_id})
        for i in range(len(data)):
            data[i] = ProjectData(data[i])
        for i in data:
            if i.id == project_id:
                return i
        return None

    def get_user_project(self, user_id : str, project_id : str):
        """
            user_id : str
            project_id : str
            returns: user project data
            description: Get user project data
        """
        user = self.__ftlib.Users.get_user_by_login(user_id).id
        data = self.__api.page("/v2/projects/{}/projects_users".format(project_id), params={'filter[user_id]': user})
        return data

    def get_user_projects(self, user_id : str):
        """
            user_id : str
            returns: list of user projects
            description: Get user projects
        """
        data = self.__api.page("/v2/users/{}/projects_users".format(user_id))
        return(data)
    
    def get_project_user_by_id(self, ids : int):
        """
            ids : int
            returns: list of project users
            description: Get project users by id
        """
        data = self.__api.page("/v2/projects_users", params={"filter[id]": ids})
        return data

    def get_teams_by_project_session_id(self, project_session_id : int, created_at : str = None, updated_at : str = None, deadline_at : str = None, status : str = None):
        """
            project_id : int
            returns: list of teams
            description: Get teams by project id
        """
        params = {}
        if created_at != None:
            params["filter[created_at]"] = created_at
        if updated_at != None:
            params["filter[updated_at]"] = updated_at
        if deadline_at != None:
            params["filter[deadline_at]"] = deadline_at
        if status != None:
            params["filter[status]"] = status
        data = self.__api.page("/v2/project_sessions/{}/teams".format(project_session_id), params=params)
        return data


    def set_title(self, user_id : str):
        pass
__all__ = ["Projects"]
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")