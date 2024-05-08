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


from multiprocessing import Process
def runConcurrently(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


import multiprocessing


def runConcurrently(func1, func2, arg):
    # Create processes for each function
    process1 = multiprocessing.Process(target=func1, args=(arg,))
    process2 = multiprocessing.Process(target=func2, args=(arg,))
    
    # Start both processes
    process1.start()
    process2.start()
    
    # Wait for both processes to finish
    process1.join()
    process2.join()

if __name__ == "__main__":
    # Define the argument
    argument = ...
    
    # Call the function to run both functions in parallel
    run_functions_in_parallel(function1, function2, argument)
