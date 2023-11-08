import sqlite3

connection = sqlite3.connect('./SQLITE_DB/data.db')

cursor = connection.cursor()

# Create the DISCVR Data Table
cursor.execute("CREATE TABLE IF NOT EXISTS data_in"
               "(time NOT NULL UNIQUE,bt,bx_gse,by_gse,bz_gse,theta_gse,phi_gse,"
               "bx_gsm,by_gsm,bz_gsm,theta_gsm,phi_gsm"
               ")")
# Create the Planetary Kp Index Table
cursor.execute("CREATE TABLE IF NOT EXISTS data_validate"
               "(time NOT NULL UNIQUE,"
               "kp_index,"
               "estimated_kp,kp"
               ")")

connection.close()
