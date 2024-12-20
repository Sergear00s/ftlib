import ftlib
import json


app = ftlib.Ftlib(UID, SECRET)

#users = app.Users.get_users_by_logins(["itest"])


#journal = app.Journal.get_list(ftlib.CAMPUS_ISTANBUL, ["miskirik"], "2024-10-01", "2024-11-30")


#campus_users = app.Users.get_campus_users(ftlib.CAMPUS_ISTANBUL)
#user = app.Users.get_user_by_login("miskirik")


#data = app.Cursus.get_campus_cursus_users(ftlib.CAMPUS_ISTANBUL, ftlib.COMMON_CORE_ID)


# data = app.Cursus.get_cursuses_datas(["itest], ftlib.CAMPUS_ISTANBUL)


data = app.Users.location_stats("login", begin_at="2022-02-01")
with open("./example/data.json", "w") as file:
    json.dump(data , file, indent=4)


#print(len(campus_users))









