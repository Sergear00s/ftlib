
import requests



class Projects():

    def __init__(self, api) -> None:
        self.__api = api

    def update_project_mark(self, project_id : int, final_mark : int) -> None:
        """
            project_id : int
            final_mark : int
            description: Update project mark
        """
        resp = requests.patch(f"{self.__api.endpoint}/v2/projects_users/{project_id}", headers=self.__api.header, data={
             "projects_user": 
             {
                 "final_mark": str(final_mark),
             }
        })
        self.__api.eval_resp(resp)
        return None
    #todo: 
    def delete_evaluate(self):
        pass


    #todo:

    def get_projects(self, cursus_id : int):
        """
            cursus_id : int
            returns: list of projects of a cursus
        """
        data = self.__api.Api.page("/v2/cursus/{}/projects".format(cursus_id))
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data
    
    def get_projects_by_list(self, project_ids : list, cursus_id):
        """
            project_ids : list
            cursus_id : int
            returns: list of projects of a cursus
        """
        project_ids_ = ", ".join(project_ids)
        data = self.__api.Api.page("/v2/cursus/{}/projects".format(cursus_id), params={"filter[id]": project_ids_})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data
    def get_project(self, project_id : int, cursus_id : int):
        """
            project_id : int
            cursus_id : int
            returns: project data of a cursus by project id
        """
        data = self.__api.Api.page("/v2/cursus/{}/projects".format(cursus_id), params={"filter[id]": project_id})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data

    def get_user_project(self, user_id : str, project_id : str):
        """
            user_id : str
            project_id : str
            returns: user project data
            description: Get user project data
        """
        user = self.__api.Users.get_user_by_login(user_id).id
        data = self.__api.Api.page("/v2/projects/{}/projects_users".format(project_id), params={'filter[user_id]': user})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data

    def get_user_projects(self, user_id : str):
        """
            user_id : str
            returns: list of user projects
            description: Get user projects
        """
        data = self.__api.Api.page("/v2/users/{}/projects_users".format(user_id))
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return(data)
    
    def get_project_user_by_id(self, ids : int):
        """
            ids : int
            returns: list of project users
            description: Get project users by id
        """
        data = self.__api.Api.page("/v2/projects_users", params={"filter[id]": ids})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
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
        data = self.__api.Api.page("/v2/project_sessions/{}/teams".format(project_session_id), params=params)
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data


    def set_title(self, user_id : str):
        pass
__all__ = ["Projects"]
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")