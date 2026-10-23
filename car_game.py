car_input=input()
if car_input.lower()=="help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit the game")
    
    while car_input.lower()!="quit":
        car_input=input()
        if car_input.lower()=="start":
            print("Car started...Ready to go!")
            car_input=input()
        elif car_input.lower()=="stop":
            print("Car stopped.")   
            car_input=input()
        elif car_input.lower()=="quit":
            print("Game exited.")
else:
    print("I don't understand that...")
#check understanding of the code 1hr 35 mins to 41 mins