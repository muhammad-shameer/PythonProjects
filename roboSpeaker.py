import os

if __name__ == "__main__":
  
    print("RoboSpeaker 1.1 Created & Tested by Shameer")  # Title

    while True: # infinte loop
        userInput = input("Enter what you wish for me to say (q to quit)\n")
        if userInput == 'q':
            print("Exiting...")
            break

        else:
            command = f"say {userInput}"
            os.system(command)
