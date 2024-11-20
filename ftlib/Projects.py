

import requests


class Projects():
    def __init__(self, api) -> None:
        self.__api = api
    
    def update_project_mark(self, project_id : int, final_mark : int):

        """https://api.intra.42.fr/v2/projects_users/:id"""

        resp = requests.patch(f"{self.__api.endpoint}/v2/projects_users/{project_id}", headers=self.__api.header, data={
             "projects_user": 
             {
                 "final_mark": str(final_mark),
             }
        })
        self.__api.eval_resp(resp)
        
    
    #todo: 
    def delete_evaluate(self):
        pass


    #todo:

    def get_user_projects(self, user):
        """/v2/users/:user_id/projects_users"""
        pass