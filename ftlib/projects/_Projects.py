
import requests



class Projects():

    def __init__(self, api) -> None:
        self.__api = api


    def update_project_mark(self, project_id : int, final_mark : int) -> None:

        """https://api.intra.42.fr/v2/projects_users/:id"""

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
    def get_user_project(self, user_id : str, project_id : str):
        """/v2/projects/:project_id/projects_users"""
        user = self.__api.Users.get_user_by_login(user_id).id
        data = self.__api.Api.page("/v2/projects/{}/projects_users".format(project_id), params={'filter[user_id]': user})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data

    def get_user_projects(self, user_id : str):
        """/v2/users/:user_id/projects_users"""
        data = self.__api.Api.page("/v2/users/{}/projects_users".format(user_id))
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return(data)
        pass
    
    def get_project_user_by_id(self, ids : int):
        """/v2/projects_users"""
        data = self.__api.Api.page("/v2/projects_users", params={"filter[id]": ids})
        data = self.__api.format_page_resp(data)
        data = self.__api.extract(data)
        return data

    def set_title(self, user_id : str):
        pass
__all__ = ["Projects"]
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")