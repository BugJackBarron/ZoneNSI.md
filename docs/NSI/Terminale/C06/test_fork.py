# Python program to explain os.fork() method 

# importing os module 
import os, time


# Create a child process
# using os.fork() method 
pid = os.fork()

# pid greater than 0 represents
# the parent process 
if pid > 0 :
    print("I am parent process:")
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)

# pid equal to 0 represents
# the created child process
else :
    print("\nI am child process:")
    print("Process ID:", os.getpid())
    print("Parent's process ID:", os.getppid())

a = 0
for i in range(10000):
    a += a**3
    time.sleep(0.001)
print(f"Finished {os.getpid()}")



# If any error occurred while
# using os.fork() method
# OSError will be raised
