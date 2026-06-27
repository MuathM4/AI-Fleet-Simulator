import requests
import time
import csv
import os
from datetime import datetime

# --- Settings ---
API_URL = "http://192.168.0.120:25555/api/ets2/telemetry"
CSV_FILE = "aid_transport_ground_truth.csv"
LOGGING_INTERVAL = 1.0  # Time between reads in seconds

# Columns for our CSV file, now including Advanced Dynamics (Steering & G-Forces)
HEADERS = [
    "Timestamp", 
    "Source_City", "Destination_City", "Cargo", "Cargo_Mass_kg",
    "Speed_kmh", "Speed_Limit_kmh", "RPM", "Gear", "Throttle", "Brake", "Steering",
    "Accel_X", "Accel_Y", "Accel_Z",
    "Engine_Wear_%", "Tire_Wear_%", "Chassis_Wear_%",
    "Fuel_%", "Driving_Status"
]

def get_driving_status(speed, speed_limit, fuel_percent, brake_input, accel_x):
    statuses = []
    
    # 1. Speeding: (باقية كما هي)
    if speed_limit > 0 and speed >= speed_limit:
        statuses.append("Speeding")
        
    # 2. Hard Braking: (أضفنا شرط السرعة لمنع تسجيلها والشاحنة واقفة)
    if brake_input > 0.8 and speed > 15:
        statuses.append("Hard Braking")
        
    # 3. Harsh Cornering: (اعتمدنا على قوة الجاذبية الجانبية بدلاً من الدركسون)
    # 0.3 تعتبر قوة طرد مركزي ملحوظة (G-Force) أثناء الانعطاف
    if speed > 20 and abs(accel_x) > 0.3:
        statuses.append("Harsh Cornering")
        
    # 4. Low Fuel:
    if fuel_percent < 15:
        statuses.append("Low Fuel")
        
    return " | ".join(statuses) if statuses else "Normal"

def main():
    file_exists = os.path.isfile(CSV_FILE)
    
    print("🚀 A'id Transport Logger (Advanced Dynamics Edition) Started...")
    print("-" * 60)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(HEADERS)
            print("📝 Created new file with advanced telemetry column names.")

        while True:
            start_time = time.time()  
            
            try:
                response = requests.get(API_URL, timeout=0.5)
                data = response.json()

                # 1. Job details
                job = data.get("job", {})
                source_city = job.get("sourceCity", "None")
                dest_city = job.get("destinationCity", "None")
                cargo = job.get("cargo", "None")
                cargo_mass = job.get("mass", 0)

                # 2. Basic Driving data
                truck = data.get("truck", {})
                speed_kmh = truck.get("speed", 0)
                rpm = truck.get("engineRpm", 0)
                gear = truck.get("displayedGear", 0)
                throttle = truck.get("userThrottle", 0.0)
                brake = truck.get("userBrake", 0.0)
                
                # 3. Advanced Dynamics (Steering and Acceleration/G-Forces)
                steering = truck.get("userSteer", 0.0)
                acceleration = truck.get("acceleration", {})
                accel_x = acceleration.get("x", 0.0)
                accel_y = acceleration.get("y", 0.0)
                accel_z = acceleration.get("z", 0.0)

                # 4. Navigation & Speed Limit
                nav = data.get("navigation", {})
                speed_limit = nav.get("speedLimit", 0)

                # 5. Truck health and fuel
                engine_wear = round(truck.get("wearEngine", 0) * 100, 2)
                tire_wear = round(truck.get("wearWheels", 0) * 100, 2)
                chassis_wear = round(truck.get("wearChassis", 0) * 100, 2)
                
                current_fuel = truck.get("fuel", 0)
                fuel_capacity = max(truck.get("fuelCapacity", 1), 1)
                fuel_percent = round((current_fuel / fuel_capacity) * 100, 1)

                # 6. Evaluate driving status using the new steering metric
                driving_status = get_driving_status(speed_kmh, speed_limit, fuel_percent, brake, steering)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                # 7. Construct and append the row
                row = [
                    timestamp,
                    source_city, dest_city, cargo, cargo_mass,
                    round(speed_kmh, 1), speed_limit, round(rpm, 1), gear, round(throttle, 2), round(brake, 2), round(steering, 2),
                    round(accel_x, 3), round(accel_y, 3), round(accel_z, 3),
                    engine_wear, tire_wear, chassis_wear,
                    fuel_percent, driving_status
                ]
                
                writer.writerow(row)
                file.flush()

                print(f"[{timestamp}] Speed: {int(speed_kmh)} km/h | Accel_Z: {round(accel_z, 2)} | Status: {driving_status}")

            except requests.exceptions.RequestException:
                print("⚠️ Could not connect to the game")
            except KeyError as e:
                print(f"⚠️ Missing data from the game: {e}")
            except Exception as e:
                print(f"⚠️ Error: {e}")

            elapsed_time = time.time() - start_time
            sleep_time = max(0.0, LOGGING_INTERVAL - elapsed_time)
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()