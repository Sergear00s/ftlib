import ftlib
import json
import dotenv
import os

dotenv.load_dotenv()
UID=os.getenv("UID")
SECRET=os.getenv("SECRET")
app = ftlib.Ftlib(UID, SECRET)


# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)