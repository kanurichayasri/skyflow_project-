import joblib
import numpy as np
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_mission_planner():
    if not os.path.exists('skyflow_model.pkl'):
        print("Error: SkyFlow Core missing. Run 'python drone_physics_sim.py' first.")
        return

    model = joblib.load('skyflow_model.pkl')
    
    clear_screen()
    print("="*60)
    print("       SKYFLOW: DRONE MISSION ENDURANCE ESTIMATOR      ")
    print("="*60)
    print("Enter Pre-Flight Parameters:\n")

    try:
        payload = float(input("Payload Weight (kg): "))
        wind = float(input("Current Wind Speed (km/h): "))
        battery = float(input("Battery Health Condition (%): "))
        alt = float(input("Target Cruise Altitude (m): "))

        # Prepare for prediction
        input_data = np.array([[payload, wind, battery, alt]])
        prediction = model.predict(input_data)[0]

        print("\n" + "-"*60)
        print(f"PREDICTED MAX ENDURANCE: {prediction:.1f} MINUTES")
        print("-"*60)
        
        if prediction < 15:
            print("MISSION STATUS: [REJECTED] - High risk of power depletion.")
        elif prediction < 25:
            print("MISSION STATUS: [CAUTION] - Short-range missions only.")
        else:
            print("MISSION STATUS: [GO] - Safe for deployment.")
        print("-"*60 + "\n")

    except ValueError:
        print("\n[Input Error] Please enter numerical data for flight parameters.")

if __name__ == "__main__":
    run_mission_planner()