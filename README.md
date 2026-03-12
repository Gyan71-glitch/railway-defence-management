# Railway Defence Management System 🚆

An AI-based railway safety monitoring prototype that detects hazards on railway tracks using computer vision and generates alerts.

## Overview

This system simulates an intelligent railway monitoring node that:

* Captures camera frames
* Detects objects using YOLO-based AI
* Evaluates hazard severity
* Logs alerts to a database
* Displays alerts on a dashboard

## Features

* Real-time camera monitoring
* AI object detection
* Hazard severity classification
* Alert logging (CSV / database)
* Web dashboard for monitoring

## Tech Stack

* Python
* OpenCV
* YOLOv8
* Flask
* SQLite

## Project Structure

core/ – AI detection, alert logic, GPS simulation
templates/ – Dashboard UI
main.py – Main detection pipeline
cloud_server.py – Alert dashboard server

## Running the Project

Install dependencies

pip install -r requirements.txt

Run the dashboard

python cloud_server.py

Run detection

python main.py
