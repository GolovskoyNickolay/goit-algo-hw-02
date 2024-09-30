from queue import Queue
import random
import time

queue = Queue()


def generate_request():
    request_id = random.randint(1, 100)
    queue.put(f"Request {request_id}")
    print(f"Generated: Request {request_id}")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty!")


while True:
    generate_request()
    process_request()
    time.sleep(1)
