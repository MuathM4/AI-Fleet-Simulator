import json
import requests
import time

while True:
    
 response = requests.get("http://172.25.125.228:25555/api/ets2/telemetry")
 live_data = json.loads(response.text)
 print("Server response is: ", response.text)

 speed_kmh = int(live_data["truck"]["speed"])
 speed_limit = 50
 print("Current Speed in Km/h: ", int(speed_kmh))

 if speed_limit <= speed_kmh:
  with open("sahir_log.txt", "a", encoding="utf=8") as file:
   file.write(f"Speed is: {speed_kmh} km/h\n")
   print("The speed is too much, penalty logged... ")

 
 
 "Test Failed: Higher Speed than 50km/h in city"
 print("Test Succeed: Lower or equal Speed 50km/h")

 time.sleep(1)

 current_fuel = live_data["truck"]["fuel"]
 current_fuel_int = int(live_data["truck"]["fuel"])
 fuel_capacity = live_data["truck"]["fuelCapacity"]

 fuel_per = int((current_fuel/fuel_capacity) * 100)
 print(f"Current fuel is: {fuel_per} and has ({current_fuel_int} litters...)")

 if fuel_per < 15:
    with open("sahir_log.txt", "a", encoding="utf=8") as file:
     file.write(f"Fuel is: {fuel_per} and needs to refuel\n")
     print("The fuel is too low, you should visit the station... ")