from prefect import flow, task, serve
import random
import time

@task
def _connect_rob2():
    # Connect to robot
    print("At _connect_rob2()")
    time.sleep(5)  # wait 5 seconds


@flow
def main():
    print("Starting run_2...")
    try:
        serve(
            _connect_rob2()
        )
    except Exception as e:
        print(f"[flow] Error during flow execution: {e}")
    finally:
        print("Flow finished (success or error).")

if __name__ == "__main__":
    main()
