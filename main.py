import sys
import time  # Library for handling time
import threading  # Library for managing concurrent tasks


class Clock:
    """
    A class to simulate a clock with customizable messages for different time intervals.

    Attributes:
        duration_hours (int): The duration of the clock in hours.
        tick_message (str): The message for each second.
        tock_message (str): The message for each minute.
        bong_message (str): The message for each hour.
        running (bool): A flag to control the running state of the clock.
    """

    def __init__(self, duration_hours=3, tick_message="tick", tock_message="tock", bong_message="bong"):
        """
        Initializes the Clock object with default or user-provided parameters.

        Args:
            duration_hours (int, optional): The duration of the clock in hours. Defaults to 3 hours.
            tick_message (str, optional): The message for each second. Defaults to "tick".
            tock_message (str, optional): The message for each minute. Defaults to "tock".
            bong_message (str, optional): The message for each hour. Defaults to "bong".
        """
        self.duration_hours = duration_hours
        self.tick_message = tick_message
        self.tock_message = tock_message
        self.bong_message = bong_message
        self.running = True
        self.stop_time = time.time() + self.duration_hours * 3600

    def run(self):
        """
        Starts the clock simulation.
        """
        self.running = True

        def print_clock():
            """
            Prints messages corresponding to the current time.

            This function runs in a separate thread to continuously print messages for each second, minute, and hour
            based on the current time. It stops running after the specified duration.
            """
            start_time = time.time()  # Record the starting time of the clock
            while self.running:  # Continue printing messages until the clock stops
            # while self.running:  # Continue printing messages until the clock stops

                current_time = time.localtime()  # Get the current time
                if current_time.tm_sec == 0 and current_time.tm_min == 0:
                    print(self.bong_message)  # Print a message for every new hour
                elif current_time.tm_sec == 0:
                    print(self.tock_message)  # Print a message for every new minute
                else:
                    print(self.tick_message)  # Print a message for every second
                time.sleep(1)  # Wait for 1 second

                #  Check if the current time exceeds the stop time
                if time.time() >= self.stop_time:
                    self.running = False  # Stop the clock

        clock_thread = threading.Thread(target=print_clock)  # Create a thread to run the print_clock function
        clock_thread.start()  # Start the thread

        def input_thread():
            """
            Allows the user to customize messages for the clock.

            This function runs in a separate thread to continuously prompt the user to enter new messages for
            each time interval (tick, tock, bong) while the clock is running.
            """
            while self.running:  # Continue handling user input until the clock stops
                # Ask the user for message choice
                message_choice = input("\nEnter message to change (tick/tock/bong) or press Enter to skip: \n")
                # Check the user's choice and update messages accordingly
                if message_choice.lower() == "tick":
                    self.tick_message = input("\nEnter new message for tick: \n")
                elif message_choice.lower() == "tock":
                    self.tock_message = input("\nEnter new message for tock: \n")
                elif message_choice.lower() == "bong":
                    self.bong_message = input("\nEnter new message for bong: \n")
                elif message_choice.lower() == "":
                    continue
                else:
                    print("Invalid choice!")

        input_thread = threading.Thread(target=input_thread)  # Create a thread to run the input_thread function
        input_thread.start()  # Start the thread


if __name__ == "__main__":
    clock = Clock(duration_hours=0.1)  # Create an instance of the Clock class
    clock.run()  # Start the clock simulation
