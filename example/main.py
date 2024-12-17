import ftlib
import json



app = ftlib.Ftlib(UID, SECRET)


#users = app.Users.get_users_by_logins(["itest"])


#journal = app.Journal.get_list(ftlib.CAMPUS_ISTANBUL, ["miskirik"], "2024-10-01", "2024-11-30")


#campus_users = app.Users.get_campus_users(ftlib.CAMPUS_ISTANBUL)
user = app.Users.get_user_by_login("itest")

a = json.dumps(app.Cursus.get_cursus(user.login, ftlib.COMMON_CORE_ID), indent=4)

print(a)

#print(len(campus_users))









