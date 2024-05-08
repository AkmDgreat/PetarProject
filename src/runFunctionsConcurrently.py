import threading

def runConcurrently(func1, func2):
    # Create threads
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

    print("Both functions completed.")