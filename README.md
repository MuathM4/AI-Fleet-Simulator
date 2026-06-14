# Fleet Management Simulator (Using ETS2)

I basically built a live dashboard to track big trucks, In a new and creative to improve simulations for logistics and telemmatics companies.

instead of buying an actual truck and expensive tracking hardware, I used Euro Truck Simulator 2 to get realistic driving data. basically making testing more productive.

## How this work

connect a truck driving in the game to a live website. when the truck moves, loses fuel, changes gears - the website updates instantly. like a control room for a shipping company but for a game truck.

## how i built it

kept it simple:

1. **ETS2** - the game just runs and generates real physics data (speed, rpm, gear, fuel)
2. **Python + Flask backend** - pulls the live truck data and converts it to json that makes sense
3. **HTML + JavaScript frontend** - refreshes every half second to show what's happening. it's a web page that stays in sync with the game

## what's in here

- simulation environment: Euro Truck Simulator 2
- server: Python & Flask
- interface: HTML5 & JavaScript (fetching data live)

## why i built this

wanted to understand how real IoT devices and fleet tracking actually work. this project shows you can take massive amounts of data from a simulator and display it smoothly on a web page without everything getting slow. useful if you're building something similar for actual vehicles

pretty cool to watch a dashboard update in real-time while you're driving a truck through digital Europe
