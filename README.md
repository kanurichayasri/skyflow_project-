# skyflow_project-
SkyFlow: Drone Mission Endurance and Payload Estimator
Project Overview
SkyFlow is a machine learning-based flight planning tool developed for Unmanned Aerial Systems (UAS). In drone logistics and aerial survey operations, estimating battery endurance is a critical safety requirement. Traditional battery percentages often fail to account for external physical factors like payload weight, wind resistance, and air density.

This project utilizes a Random Forest Regressor to predict the "Maximum Safe Flight Time" (Endurance) by analyzing real-time telemetry and environmental conditions. By providing a data-driven "Go/No-Go" status, SkyFlow helps prevent mid-air power depletion and ensures mission safety.

Environment Setup and Requirements
To run this project, you will need Python 3.8 or higher installed on your system.

1. Clone the Repository
Open your terminal and run the following commands to get the project files:
git clone https://github.com/kanurichayasri /SkyFlow-Aerospace
cd SkyFlow-Aerospace

2. Install Dependencies
This project requires pandas, scikit-learn, joblib, and numpy. You can install all necessary libraries using the provided requirements file:
pip install -r requirements.txt

Execution Instructions
SkyFlow follows a professional "Train-then-Predict" workflow. Please execute the scripts in the following order:

Step 1: Model Training (The Backend)
Run the training script to generate the synthetic flight dataset, train the Random Forest model, and save the intelligence as a local file.
python drone_physics_sim.py

Note: Once successful, a file named 'skyflow_model.pkl' will be generated in your project directory.

Step 2: Mission Planning Tool (The CLI)
Once the model is trained, you can use the interactive command-line interface to get mission safety recommendations.
python skyflow_cli.py

Usage: Enter the requested flight parameters (Payload, Wind Speed, Battery Health, and Altitude) when prompted to receive an instant endurance estimate and mission status.

Technical Implementation Details
Algorithm: Random Forest Regressor (chosen for its ability to handle non-linear relationships between aerodynamics and power draw).

Dataset: 3,000 simulated mission profiles incorporating variable wind vectors and battery degradation curves.

Safety Logic: The system includes a 5-minute "Emergency Reserve" calculation to ensure drones never reach 0% power while still in flight.

Model Persistence: Joblib is used for serialized model storage, allowing for rapid field deployment without retraining.

Project Structure
drone_physics_sim.py: The training engine and data generation logic.

skyflow_cli.py: The interactive mission planning interface for the operator.

requirements.txt: List of all necessary Python libraries.


