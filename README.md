# Purpose

This code is for sensors and an autopilot system for drowsy or intoxicated car drivers. When the driver becomes drowsy or drunk while driving, the sensors activate and the autopilot takes control of the car, steering it to the roadside to find a safe spot until the driver regains full awareness.

## Driver Monitoring & Auto-Pilot Simulation

This project simulates a **driver monitoring system** with **automatic pilot assist**.  
It uses OpenCV to detect drowsiness (closed eyes) or random alcohol influence, and engages a simulated autopilot that "pulls the car over safely".

## Features
- Detects driver's eyes (open/closed) using OpenCV.
- Triggers drowsiness detection if eyes remain closed for more than 5 seconds.
- Randomly simulates alcohol impairment.
- Engages "autopilot mode" (slows down, finds roadside spot, pulls over).
- Runs on webcam for live testing.

## 🔹 Simulation Features:
- Camera/Webcam → used to detect face & driver’s eyes.
- If eyes are closed > 5 seconds → system assumes drowsy.
- There’s a random event (10%) to simulate alcohol detection.
- When detected → autopilot activates, simulating a pull-over with step-by-step printed logs.
- Drowsiness detection (PERCLOS, EAR, yawning) from the camera using MediaPipe Face Mesh.
- Optional reading of an alcohol sensor (e.g., MQ-3) via Serial from a microcontroller (Arduino).
- Autopilot state machine that “pulls over” in the simulation (using Pygame) when the driver is unsafe.
- Can be stopped by pressing q.

## ⚠️ Warning
- This is a simulation (not a real system for cars).
- For real implementation you would need: 
- Camera + AI (face/eyelid detection)
- Alcohol sensor
- Hand pressure sensor on steering wheel
- And a car control system, which is much more complex and very risky if directly applied.
- This project is for simulation and educational purposes only. It is NOT a real self-driving or safety system. Do not use it in actual vehicles.
- this code is only for learning/simulation on desktop. Real-world vehicle automation systems require automotive-grade sensors, automotive-grade verification, safety validation, certification, and extensive testing. Do not use this to drive real vehicles.

## Technical Challenges
- Accurate detection of drowsiness/intoxication requires a combination of camera sensors (eye-tracking), physiological sensors (heart rate, steering wheel grip), and AI.
- A real autopilot is not just about coding Arduino, but requires integration into the drive-by-wire system, GPS, LIDAR, cameras, and vehicle control systems.
- Safety aspects are highly critical (misdetection must not occur, as it can be dangerous).

## Potential Step-by-Step Realization
- Can start with a simple simulation (like the Python code I created).
- The next level could be building a small hardware prototype: Arduino/Raspberry Pi + DHT/IR/accelerometer sensor + relay/servo motor module.
- Advanced stage → integration with a real car (requires collaboration with automotive engineers).

## How to Run
```bash
pip install -r requirements.txt
python src/main.py bash```

## Support Me
If you find this project useful, you can support me on [ko-fi.com](https://www.ko-fi.com/codesnack).
