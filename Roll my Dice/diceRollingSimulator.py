import cv2
import random

def rollDice():
    video = cv2.VideoCapture(r'./animation.mp4')
    video.set(cv2.CAP_PROP_FPS, 200)
    
    i = 1
    while(video.isOpened()):
        i+=1
        if(i>50):
            ret, frame = video.read()
            if(i>251):
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if(ret):
                cv2.imshow('Rolling Dice',frame)
            else:
                break
    print("You got "+str(getRandomNumber()))
    video.release()
    cv2.destroyAllWindows()
    
def getRandomNumber():
    return random.randint(1,6)

def main():
    repeat = True
    while repeat:
        rollDice()
        s = input("Press Enter to roll again or 'q' to quit\n")
        if(s.lower() == "q"):
            repeat = False
            print("\nThanks for playing!..")
        else:
            print("Rolling Again..")
            
print("Rolling Dice Simulator\nRolling Dice Now...")   
main()