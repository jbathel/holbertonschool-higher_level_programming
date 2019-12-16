#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name
        FROM cities INNER JOIN states ON
        cities.state_id=states.id
        WHERE states.name=%s""", (argv[4], ))
    query_rows = cur.fetchall()
    results = []
    seperator = ', '
    for row in query_rows:
        results.append(row[0])
    print(seperator.join(results))
    cur.close()
    conn.close()
