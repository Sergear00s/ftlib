

class Scale_teams:
    def __init__(self, ftlib) -> None:
        self.__ftlib = ftlib


    def get_scale_team_as_corrector_by_user(self, user_id : int):
        """
            user_id : int
            returns: list of scale teams where the user is a corrector
        """
        data = self.__ftlib.Api.page("/v2/users/{}/scale_teams/as_corrector".format(user_id))
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return(data)
    
    def get_scale_team_as_corrected_by_user(self, user_id : int):
        """
            user_id : int
            returns: list of scale teams where the user is a corrected
        """
        data = self.__ftlib.Api.page("/v2/users/{}/scale_teams/as_corrected".format(user_id))
        data = self.__ftlib.format_page_resp(data)
        data = self.__ftlib.extract(data)
        return(data)
    

    def delete_scale_team(self, scale_team_id : int):
        """
            scale_team_id : int
            description: Delete a scale team
        """
        data = self.__ftlib.Api.delete("/v2/scale_teams/{}".format(scale_team_id))
        return data