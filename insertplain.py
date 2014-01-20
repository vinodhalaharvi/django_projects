import psycopg2
import sys
def getlines():
	"""docstring for getlines"""
	for line in sys.stdin.readlines():
		line = line.strip()
		search, code = line.split()
		yield (search, code)

if __name__ == '__main__':
	con = psycopg2.connect("dbname=django_projects user=admin password=admin")
	cur = con.cursor()
	cur.executemany("insert into pyjunkee_code(search, code) values (?, ?) ", [("test", "test")])
	con.commit()
	print cur.fetchall()
