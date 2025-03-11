import ftlib
import json
import dotenv
import os


from ftlib import Cursus, Exam, Projects, Scale_teams
dotenv.load_dotenv()
UID=os.getenv("UID")
SECRET=os.getenv("SECRET")
app = ftlib.Ftlib(UID, SECRET)

cursus = Cursus(app)
data = cursus.get_campus_cursus_users(49, 21)
#data = cursus.get_campus_cursus_users(49, 21)
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)