from flask import Flask, render_template
import MySQLdb as mdb

app = Flask(__name__ , static_folder='plots')

@app.route('/realm')
def Realmdata():

    con = mdb.connect(host = 'localhost', 
                  user = 'root',
                  database = 'realmdata',
                  passwd = 'dwdstudent2015', 
                  charset='utf8', use_unicode=True);

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT char_id, char_name, death_cause, date, char_stats, base_fame, total_fame FROM recent_deaths LIMIT 100")
    stations = cur.fetchall()
    cur.close()
    con.close()
    
    
    return render_template('index.html', stations=stations)

@app.route('/plots/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#http://52.44.93.5:5000/realm
    
