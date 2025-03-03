import ftlib
import json
import dotenv
import os

dotenv.load_dotenv()
UID=os.getenv("UID")
SECRET=os.getenv("SECRET")
app = ftlib.Ftlib(UID, SECRET)

data = app.Projects.get_teams_by_project_session_id(6291, status="waiting_for_correction")

fm_data = []
for x in data:
    if x["created_at"][:4] == "2025":
        fm_data.append(x)

with open("data.json", "w") as f:
    json.dump(fm_data, f, indent=4)