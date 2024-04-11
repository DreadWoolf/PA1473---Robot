# from threading import Thread


# randomdict = {
#     "hej": 2
# }

# print(randomdict["hej"])

# randomdict["hej"] = 5

# print(randomdict["hej"])

# print(randomdict)

# randomdict["test"] = 3

# print(randomdict["test"])
# print(randomdict)

from threading import Thread
import time

def task1():
    for i in range(5):
        print("Task 1 executing...")
        time.sleep(1)
    
            
    

def task2():
    for i in range(10):
        print("Task 2 executing...")
        time.sleep(1)

if __name__ == "__main__":
    # Create two threads for each task
    thread1 = Thread(target=task1)
    thread2 = Thread(target=task2)

    # Start the threads
    thread1.start()
    thread2.start()

    # # Wait for both threads to finish
    # thread1.join()
    # thread2.join()

    print("Both tasks are completed.")
