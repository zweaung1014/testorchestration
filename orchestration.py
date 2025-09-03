from prefect import flow, task
import random
import time

@task
def _connect_rob():
    # Connect to robot
    print("At _connect_rob()")
    time.sleep(5)  # wait 5 seconds

@task
def home():
    try:
        print("At home")
        time.sleep(5)  # wait 5 seconds
        # Example risky code
        if random.choice([True, False]):
            raise ValueError("Something went wrong at home")
    except Exception as e:
        print(f"[home task] Error: {e}")
        # You could log, retry, or re-raise depending on how you want Prefect to behave
        # raise e  

@flow
def pick_up_salsa():
    try:
        print("Picked up salsa")
        home()
        _connect_rob()
        # Example risky code
        if random.choice([True, False]):
            raise RuntimeError("Couldn't pick up salsa")
    except Exception as e:
        print(f"[pick_up_salsa task] Error: {e}")
        # raise e   # uncomment if you want the flow to fail when this happens

@flow
def main():
    print("Starting run...")
    try:
        home()
        pick_up_salsa()
    except Exception as e:
        print(f"[flow] Error during flow execution: {e}")
    finally:
        print("Flow finished (success or error).")

if __name__ == "__main__":
    main()
