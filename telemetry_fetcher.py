import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# السماح لصفحة الويب بالدخول دون أي قيود أمنية
CORS(app)

# رابط السيرفر الوسيط بالـ IP الصريح والمسار المتوافق مع نسختك
ETS2_SERVER_URL = "http://127.0.0.1:2555/api/telemetry"

@app.route('/api/fleet/telemetry', methods=['GET'])
def forward_telemetry():
    try:
        # بايثون يجلب البيانات من السيرفر الوسيط بأمان وبدون حظر شبكة
        response = requests.get(ETS2_SERVER_URL, timeout=1)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("isGameConnected"):
                truck_data = data.get("truck", {})
                
                # تجميع البيانات الجاهزة والمستقرة القادمة من برنامج Funbit
                telemetry_payload = {
                    "isGameConnected": True,
                    "truck_id": "SA-TRUCK-01",
                    "truck_name": truck_data.get("make", "Volvo"),
                    "telemetry": {
                        "speed": round(truck_data.get("speed", 0), 1),
                        "fuel_liters": round(truck_data.get("fuel", 0), 1),
                        "gear": truck_data.get("displayedGear", 0),
                        "engine_rpm": round(truck_data.get("engineRpm", 0), 0)
                    }
                }
                return jsonify(telemetry_payload), 200
            else:
                return jsonify({"isGameConnected": False, "message": "Game running but in menu"}), 200
        else:
            return jsonify({"isGameConnected": False, "message": "Server error"}), 500

    except requests.exceptions.ConnectionError:
        return jsonify({"isGameConnected": False, "message": "Cannot connect to Funbit Server"}), 503

if __name__ == "__main__":
    print("\n[SUCCESS] Data Bridge Gateway is running...")
    print("[INFO] Web App should fetch from: http://127.0.0.1:5000/api/fleet/telemetry")
    app.run(host='127.0.0.1', port=5000, debug=False)