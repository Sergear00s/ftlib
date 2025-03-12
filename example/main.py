import ftlib
import json
import dotenv
import os


dotenv.load_dotenv()
UID=os.getenv("UID")
SECRET=os.getenv("SECRET")


lib = ftlib.ftlib(ftlib.Credentials(UID, SECRET))
data = lib.Exam.get_exams(49, 25)
