import ftlib
import json
import dotenv
import os
dotenv.load_dotenv()

UID=os.getenv("UID")
SECRET=os.getenv("SECRET")

app = ftlib.Ftlib(UID, SECRET)




data = app.Cursus.get_campus_cursus_users(ftlib.CAMPUS_ISTANBUL, ftlib.COMMON_CORE_ID)

ln = 0
for i in data:
    if (i["end_at"] == None and i["user"]["kind"] == "student"):
        ln += 1

with open("./example/data.json", "w") as f:
    json.dump(data, f, indent=4)