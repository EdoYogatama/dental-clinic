import sys
sys.path.append('.')

import database.dbHelper
import database.doctor

db = database.dbHelper.Database('./database/dental.db')
doctor = database.doctor.Doctor()

db.executeQuery(doctor.createSqlStatement())