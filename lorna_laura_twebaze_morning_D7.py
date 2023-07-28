# Exercise 1
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileHandler("example.txt", "w") as file:
    file.write("Hello, world!")

# At this point, the file has been automatically closed


# exercise 2
import sqlite3


class DatabaseConnection:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


with DatabaseConnection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# At this point, the database connection has been automatically closed

# Exercise 3
import threading
import multiprocessing
import time


def run_function(duration):
    start_time = time.time()
    while True:
        # Run your function here
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= duration:
            break


# Multithreading example
def run_with_multithreading(durations):
    threads = []
    for duration in durations:
        thread = threading.Thread(target=run_function, args=(duration,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


# Multiprocessing example
def run_with_multiprocessing(durations):
    processes = []
    for duration in durations:
        process = multiprocessing.Process(target=run_function, args=(duration,))
        process.start()
        processes.append(process)

    # Wait for all processes to complete
    for process in processes:
        process.join()


# Example usage
durations = [1, 2, 3]  # Run the function for 1 second, 2 seconds, and 3 seconds
run_with_multithreading(durations)  # Run with multithreading
run_with_multiprocessing(durations)  # Run with multiprocessing
