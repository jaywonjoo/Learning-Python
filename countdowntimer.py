import time
#user enters seconds
user_seconds = input("Please enter your desired seconds:")
user_seconds_int = int(user_seconds)

if user_seconds_int > 60 or user_seconds_int < 0:
    print("Invalid input. Seconds should be between 0 and 60.")
else:
    while user_seconds_int > 0:
        print(f"{user_seconds_int} seconds remaining...", end='\r')
        time.sleep(1)
        user_seconds_int -=1
    # Clear the previous line completely
    print(' ' * 40, end='\r')  # overwrite with blank spaces
    print("Time's up! 🎉") 
#python counts down