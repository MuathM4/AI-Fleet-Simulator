# Fleet Management Simulator (Using ETS2)

Hi! This is my project where I built a live dashboard to track big trucks, just like real logistics companies do. 

Instead of buying a real truck and expensive tracking hardware, I used **Euro Truck Simulator 2 (ETS2)** as a super realistic simulator to give me live driving data.

## 🚚 What This Project Does
This app connects a truck driving in the game to a live website. When the truck drives, moves, or loses fuel inside ETS2, the website updates immediately to show the stats. It’s like a control room for a shipping company!

## 🛠️ How It Works (Step-by-Step)
I built this project in small, clean steps so everything runs perfectly:
1. **The Game (Data Source):** ETS2 simulates the real world and creates live physics data (Speed, RPM, Gear, Fuel).
2. **The Backend (Python Server):** I made a smart Python server using `Flask`. It takes the live truck data and converts it into clean numbers (JSON API).
3. **The Frontend (Web Dashboard):** I designed a simple webpage using HTML and JavaScript. It talks to the Python server every half-second to update the screen with live truck stats.

## 💻 Tech Stack
- **Simulation Environment:** Euro Truck Simulator 2
- **Backend Server:** Python & Flask
- **User Interface:** HTML5 & Live JavaScript (Fetch API)

## 🚀 Why I Built This
This project helped me understand how real IoT devices and fleet tracking apps work in the real world. It shows how we can take massive data from a vehicle simulator and show it on a web screen smoothly without making the system slow down.
