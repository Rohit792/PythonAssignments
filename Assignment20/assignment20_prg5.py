"""
Question:
Design a Python application that creates two threads named Thread1 and Thread2.
• Threadl should display numbers from 1 to 50.
• Thread2 should display numbers from 50 to 1 in reverse order.
• Ensure that:
    Thread2 starts execution only after Thread1 has completed.
• Use appropriate thread synchronizatio


"""
import threading
 
def Thread1():
    print("Thread 1 started: ")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Thread 2 started: ")
    for i in range(50, 0, -1):
        print(i)

def main():
 
   thread1 = threading.Thread(target= Thread1)

   thread2 = threading.Thread(target= Thread2)

   thread1.start()
   thread1.join()
   
   thread2.start()
   thread2.join()

if __name__ == "__main__":
    main()