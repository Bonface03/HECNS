from flask import Flask, request, jsonify # type: ignore
import json
from flask_cors import CORS, cross_origin # type: ignore
import pyttsx3 # type: ignore
import sqlite3
import logging
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Register User
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing required fields"}), 400

        hashed_password = password
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"message": "User registered successfully!"}), 201

    except sqlite3.Error as err:  # Replaced mysql.connector.Error with sqlite3.Error
        logger.error(f"Database error: {err}")
        return jsonify({"error": str(err)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

# Login User
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and user["password"] == password:
            return jsonify({"message": "Login successful!", "user": user["username"]}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401

    except sqlite3.Error as err:
        logger.error(f"Database error: {err}")
        return jsonify({"error": str(err)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

# Predict Addiction Level
@app.route('/message', methods=['POST'])
def predict_addiction_level():
    try:
        data = request.get_json()
        print(data)
        engine = pyttsx3.init() 
        rate = engine.getProperty('rate') 
        print(rate) 
        engine.setProperty('rate', 150)
        engine.setProperty('voice', 165) 
        engine.say(data["word"])
        engine.runAndWait()
        engine.endLoop()
 
        return jsonify({"predicted_addiction_level": "some_value"})

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


@app.route('/text', methods=['POST'])
def receive_message():
    try:
        data = request.get_json()  # Parse incoming JSON data
        if "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        message = data["text"]
        print(f"Received message: {message}")

        # Speak the received message
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(message)
        engine.runAndWait()

        return jsonify({"message": "Text received and spoken successfully"}), 200

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)