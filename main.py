import RPi.GPIO as GPIO
import MFRC522

#YOUR CODE HERE

if __name__ == '__main__':     # Program start from here
    print ("Program is starting ... ")
    try:
        #CALL FUNCTIONS/METHODS FROM HERE
        pass #You can remove the pass operator when you add commands to the try
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        GPIO.cleanup()  
