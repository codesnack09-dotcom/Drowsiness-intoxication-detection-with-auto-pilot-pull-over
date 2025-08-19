# Driver Monitoring & Auto-Pilot Simulation

This project simulates a **driver monitoring system** with **automatic pilot assist**.  
It uses OpenCV to detect drowsiness (closed eyes) or random alcohol influence, and engages a simulated autopilot that "pulls the car over safely".

## Features
- Detects driver's eyes (open/closed) using OpenCV.
- Triggers drowsiness detection if eyes remain closed for more than 5 seconds.
- Randomly simulates alcohol impairment.
- Engages "autopilot mode" (slows down, finds roadside spot, pulls over).
- Runs on webcam for live testing.

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
