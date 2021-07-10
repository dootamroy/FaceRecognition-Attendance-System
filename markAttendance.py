# created by Dootam Roy @2021

from datetime import datetime
from datetime import date
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)                                       # Firebase initialization.

today = date.today()


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
            date = today.strftime("%d/%m/%Y")
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {date}, {dtString}')          # saves the name and time in the attendance.csv file.

    # .............saving in FIREBASE.................#

