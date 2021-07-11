# created by Dootam Roy @2021

from datetime import datetime
from datetime import date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import Increment

cred = credentials.Certificate("attendance-system-c0ba4-firebase-adminsdk-5x755-b8777eb046.json")
firebase_admin.initialize_app(cred)  # Firebase initialization.

db = firestore.client()

today = date.today()
date = today.strftime("%d/%m/%Y")


def markAttendance(name):
    # ..............saving in CSV file................#
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {date}, {dtString}')  # saves the name and time in the attendance.csv file.
            # .............saving in FIREBASE.................#
            chk = db.collection('Students').document(
                name).get()  # check to see if the doc exists or not in the database.
            ref = db.collection('Students').document(name)
            if not chk.exists:
                ref.set({'NUM': 1})
            else:
                ref.update({'NUM': Increment(+1)})  # AUTO INCREAMENT and updation of val.

            # db.collection('Students').document(name).update({'NUM': })

            ref.collection('AttendanceRecord').add({'date': date, 'time': dtString})
