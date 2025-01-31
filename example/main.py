import ftlib
import json
import dotenv
import os
import pytz

dotenv.load_dotenv()
import datetime
UID=os.getenv("UID")
SECRET=os.getenv("SECRET")



app = ftlib.Ftlib(UID, SECRET)


#app.Exam.create_exam("test exam", datetime.datetime(2024,12,30,20,0,0,0,pytz.timezone("Asia/Istanbul")), 
 #                    datetime.datetime(2024,12,30,23,0,0,0,pytz.timezone("Asia/Istanbul")), "TEST", "10.11.0.0/0", 49, [ftlib.EXAM_RANK_2], visible=False)

# data = app.Api.get("/v2/campus/49/achievements")
 #print(data.json())
data = app.Achivement.get_campus_achivements(49)
with open("./example/data.json", "w") as f:
     json.dump(data, f, indent=4)

