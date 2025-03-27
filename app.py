from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.getenv('MYSQL_HOST', 'db'),  
    'user': 'root',
    'password': 'rootpassword',
    'database': 'testdb'
}

@app.route('/')
def home():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute("ALTER TABLE users AUTO_INCREMENT = 1")
        conn.commit()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
        """)

        cursor.execute("INSERT INTO users (name) VALUES ('The Aym')")
        conn.commit()


        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return f"Connexion réussie.\n  Utilisateurs : {users}"

    except Exception as e:
        return f"Erreur de connexion : {str(e)}"

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
