from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'usman'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    cur=mysql.connection.cursor()
    # cur.execute('''CREATE TABLE hello (num INTEGER, words VARCHAR(20))''')

    # cur.execute('''INSERT INTO example VALUES (1, 'USMAN')''')
    # cur.execute('''INSERT INTO example VALUES (2, 'SHOAIB')''')
    # cur.execute('''INSERT INTO example VALUES (3, 'SAEED')''')
    # mysql.connection.commit()

    results= cur.fetchall()
    print(results)
    return 'Done!'   #You can change retun to get names as well.


if __name__ == '__main__':
    app.run()
