# Import the main library required
from num2words import num2words
import pyttsx3

# Making a function that convert number to word 

def convert_num_to_str(num,to = 'ordinal_num'):
    num = num2words(num)
    return(num)

# Connecting the function to anither function 
# Function to speak words 
# rate = 100, volume = 1, voice = 1
def speak_number(num_in_words,rate = 150,volume = 1,voice = 1):
    engine= pyttsx3.init()
    # Set properties _before_ you add things to say
    engine.setProperty('rate', rate)
    # Set volume 0-1
    engine.setProperty('volume', volume)
    # Set voice 0-1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    engine.say(f"Your enter amount is:{num_in_words}")
    engine.runAndWait()

while True:
    try:
        num = int(input("Enter the number: "))
        num_in_words = convert_num_to_str(num)  # Convert number to words
        print(f"Number in words: {num_in_words}")  # Print the number in words
        speak_number(num_in_words)

        
        while True:
                ask = input("Want to try again? (Y/N): ").strip().upper()
                
                if ask == "Y":
                    print("Repeating...")
                    break  # Break the inner loop to continue the main loop
                elif ask == "N":
                    print("Thanks for using!")
                    exit()  # Exit the program
                else:
                    print("Invalid input! Please enter 'Y' or 'N'.")
     
        
        

    
 
    except Exception as e:
       print(f"Invalid Input Enter Only Number:!!")
    finally :
        print("I Hope This helped you a lot")

