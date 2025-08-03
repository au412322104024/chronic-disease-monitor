from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection setup (replace with your credentials)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Kalai994@',
    port=3300,
    database='health_monitor'
)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    # Extract and convert all inputs
    bp = int(data.get('bp', 0))
    sugar = int(data.get('sugar', 0))
    cholesterol = int(data.get('cholesterol', 0))
    heart = int(data.get('heart', 0))
    spo2 = int(data.get('spo2', 0))
    respiration = int(data.get('respiration', 0))
    weight = float(data.get('weight', 0))
    height = float(data.get('height', 0)) / 100  # convert cm to m
    temperature = float(data.get('temperature', 0))

    # Calculate BMI
    bmi = round(weight / (height * height), 2)

    # Store data in MySQL
    insert_query = """
        INSERT INTO patient_data 
        (bp, sugar, cholesterol, heart, spo2, respiration, weight, height, temperature, bmi)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (bp, sugar, cholesterol, heart, spo2, respiration, weight, height, temperature, bmi))
    conn.commit()

    # Simple health analysis logic
    message = f"✅ Your BMI is {bmi}. "

    if bp > 140 or sugar > 180 or cholesterol > 240 or heart > 100 or spo2 < 90 or temperature > 38:
        message += "⚠️ Health Alert: One or more values are outside the safe range. Please consult a doctor."
    elif bp < 90 or sugar < 70 or heart < 60 or spo2 < 85:
        message += "⚠️ Warning: Low readings detected. Monitor closely."
    else:
        message += "You seem stable. Keep monitoring regularly."

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)