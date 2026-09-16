
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) 


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "dipak001" 
DB_NAME = "voting_db"


def get_db_connection():
    
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
       
        return None


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email, has_voted FROM users WHERE email = %s AND password = %s", (email, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                session['user_id'] = user[0]
                session['email'] = user[1]
                session['has_voted'] = user[2]
                return redirect(url_for('home'))
            else:
                error = 'Invalid email or password. Please try again.'
    
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():

    session.clear()
    return redirect(url_for('home'))


@app.route('/candidates')
def candidates():

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM candidates")
        candidates_data = cursor.fetchall()
        conn.close()
        return render_template('candidates.html', candidates=candidates_data)
   
    return redirect(url_for('home'))


@app.route('/vote/<int:candidate_id>', methods=['GET', 'POST'])
def vote(candidate_id):
    
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if session.get('has_voted'):
        return redirect(url_for('home'))

    conn = get_db_connection()
    if not conn:
        return redirect(url_for('home'))

    cursor = conn.cursor()
    
    if request.method == 'POST':
        user_id = session['user_id']

        cursor.execute("INSERT INTO votes (user_id, candidate_id) VALUES (%s, %s)", (user_id, candidate_id))
        
        cursor.execute("UPDATE users SET has_voted = TRUE WHERE id = %s", (user_id,))
        
        conn.commit()
        conn.close()

        session['has_voted'] = True
        return redirect(url_for('results'))

    cursor.execute("SELECT * FROM candidates WHERE id = %s", (candidate_id,))
    candidate_data = cursor.fetchone()
    conn.close()

    if candidate_data:
        return render_template('vote.html', candidate=candidate_data)
    
    return redirect(url_for('candidates'))


@app.route('/results')
def results():
   
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('home'))

    cursor = conn.cursor()
    query = """
        SELECT c.id, c.name, c.party, COUNT(v.id) as vote_count
        FROM candidates c
        LEFT JOIN votes v ON c.id = v.candidate_id
        GROUP BY c.id, c.name, c.party
        ORDER BY vote_count DESC
    """
    cursor.execute(query)
    results_data = cursor.fetchall()
    conn.close()

    results_list = []
    for row in results_data:
        results_list.append({'id': row[0], 'name': row[1], 'party': row[2], 'votes': row[3]})
    
    winner = None
    if results_list and results_list[0]['votes'] > 0:
        if len(results_list) > 1 and results_list[0]['votes'] == results_list[1]['votes']:
             winner = {'name': "It's a Tie!", 'party': '', 'votes': results_list[0]['votes']}
        else:
            winner = results_list[0]


    return render_template('result.html', results=results_list, winner=winner)


if __name__ == '__main__':
    app.run(debug=True)
