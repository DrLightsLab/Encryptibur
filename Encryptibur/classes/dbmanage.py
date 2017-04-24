import psycopg2

try:
    conn = psycopg2.connect("dbname='encryptibur' user='encryptibur' host='localhost' password='3ncrypt'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
print "Printing cur: ", cur


cur.execute("""SELECT * FROM encryptibur""")
rows = cur.fetchall()

print "\nShow me the dtabases:\n"
for row in rows:
    print " ", row[0]
