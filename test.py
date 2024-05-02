#!/usr/bin/env pybricks-micropython

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
#---------vvvv--------thread- test--vvvv---- 
# from threading import Thread
# import time
# import sys

# def task1():
#     for i in range(8):
#         print("Task 1 executing...", i)
#         time.sleep(1)
#         if i == 5:
#             sys.exit()
    
            
    

# def task2():
#     for i in range(10):
#         print("Task 2 executing...")
#         time.sleep(1)

# if __name__ == "__main__":
#     # Create two threads for each task
#     thread1 = Thread(target=task1)
#     thread2 = Thread(target=task2)

#     # Start the threads
#     thread1.start()
#     thread2.start()

#     # # Wait for both threads to finish
#     # thread1.join()
#     # thread2.join()

#     print("Both tasks are completed.")
# from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# # This is the name of the remote EV3 or PC we are connecting to.
# SERVER = 'ev3dev'

# client = BluetoothMailboxClient()
# mbox = TextMailbox('greeting', client)

# print('establishing connection...')
# client.connect(SERVER)
# print('connected!')

# # In this program, the client sends the first message and then waits for the
# # server to reply.
# mbox.send('hello!')
# mbox.wait()
# print(mbox.read())
zonenum = [1,2,3,4, "done?"]

temp = True
while temp:
    test = int(input("input number: "))
    print(zonenum[test % len(zonenum)])