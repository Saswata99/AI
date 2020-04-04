
import kociemba

from ColorDetection import *

class Cube:
    def __init__(self):
        self.instruction  =  {
            "R"  : "Turn the right side a quarter turn away from you." ,
            "R'" : "Turn the right side a quarter turn towards you." ,
            "R2" : "Turn the right side 180 degrees." ,
            "L"  : "Turn the left side a quarter turn towards you." ,
            "L'" : "Turn the left side a quarter turn away from you." ,
            "L2" : "Turn the left side 180 degrees." ,
            "U"  : "Turn the top layer a quarter turn to the left." ,
            "U'" : "Turn the top layer a quarter turn to the right." ,
            "U2" : "Turn the top layer 180 degrees.",
            "D"  : "Turn the bottom layer a quarter turn to the right." ,
            "D'" : "Turn the bottom layer a quarter turn to the left." ,
            "D2" : "Turn the bottom layer 180 degrees." ,
            "B"  : "Turn the back side a quarter turn to the left." ,
            "B'" : "Turn the back side a quarter turn to the right." ,
            "B2" : "Turn the back side 180 degrees." ,
            "F"  : "Turn the front side a quarter turn to the right." ,
            "F'" : "Turn the front side a quarter turn to the left." ,
            "F2" : "Turn the front side 180 degrees."
        }
    

    def cubestring(self, sides):
        str = ''
        for face in 'URFDLB':
            str += ''.join(sides[face])
        return str


    def run(self):
        
        camera = Camera()
        sides = camera.scan()
        #unsolvedState = self.cubestring(sides)

        unsolvedState = "DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD"

        
        try:
            algorithm = kociemba.solve(unsolvedState)
            length = len(algorithm.split(' '))
        except Exception as err:
            print("Sorry, you did not scan all the sides correctly. Please try again.")
            exit()

        print("\n-------  Rubix Cube Solver   -------\n")
        print("Place the cube as, \nCenter of top:  white\t Center of front:  green\n")
        print("Solution : ", end="")
        print(algorithm, f"[{length} moves]\n\n")

        print("Steps : \n")
        for index, step in enumerate(algorithm.split(" ")):
            print(f"{index+1}.".ljust(6), f"{step}".ljust(2), f":  {self.instruction[step]}")


if __name__ == "__main__":
    Cube().run()
