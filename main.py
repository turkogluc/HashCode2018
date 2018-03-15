import operator
import math

def getDist(x1,y1,x2,y2):
    return math.fabs(x2-x1)+math.fabs(y2-y1)



class Car:
    def __init__(self, x, y,t,number):
        self.x = x
        self.y = y
        self.t = t
        self.number = number
class Ride:
    def __init__(self, base_x, base_y,dest_x,dest_y,start_t,finish_t,number):
        self.base_x = int(base_x)
        self.base_y = int(base_y)
        self.dest_x = int(dest_x)
        self.dest_y = int(dest_y)
        self.start_t = int(start_t)
        self.finish_t = int(finish_t)
        self.number = int(number)
        self.dist = getDist(self.base_x,self.base_y,self.dest_x,self.dest_y)



    def function(self):
        print("car constructed")



f = open("/home/cemal/Downloads/b_should_be_easy.in","r")
write_file = open("/home/cemal/Downloads/B.txt","w")
t = f.readline()
titles = t.split()

R = int(titles[0])
C = int(titles[1])
F = int(titles[2])
N = int(titles[3])
B = int(titles[4])
T = int(titles[5])

cars = []
rides = []
anycar=Car(1,2,3,4)
anyride=Ride(1,2,3,4,5,6,7)
print(R,C,F,N,B,T)


counter = 0
for line in f:
    tempRide = line.split()
    rides.append(Ride(tempRide[0],tempRide[1],tempRide[2],tempRide[3],tempRide[4],tempRide[5],counter))
    counter = counter + 1
for i in range(0,F):
    cars.append(Car(0,0,0,i))
sorted_rides=sorted(rides,key=operator.attrgetter('start_t'))
matrix = [[0 for x in range(F)] for y in range(N)]
asdf = [0 for x in range(F)]
for a in range(0,F):
    asdf[a]=0
while len(sorted_rides) != 0:
    for c in range(0,F):
        rides_number = []
        cont = True
        r = 0
        while cont and r<len(sorted_rides):
            if((cars[c].t+getDist(cars[c].x,cars[c].y,sorted_rides[r].base_x,sorted_rides[r].base_y)+sorted_rides[r].dist) <= T):
                if ((cars[c].t + getDist(cars[c].x, cars[c].y, sorted_rides[r].base_x,sorted_rides[r].base_y) + sorted_rides[r].dist) <= sorted_rides[r].finish_t):
                    if ((cars[c].t + getDist(cars[c].x, cars[c].y, sorted_rides[r].base_x,sorted_rides[r].base_y)) < sorted_rides[r].start_t):
                        cars[c].t = sorted_rides[r].start_t
                    cars[c].t = cars[c].t + getDist(cars[c].x, cars[c].y, sorted_rides[r].base_x,sorted_rides[r].base_y) + sorted_rides[r].dist
                    cars[c].x = sorted_rides[r].dest_x
                    cars[c].y = sorted_rides[r].dest_y
                    matrix[c].append(sorted_rides[r])
                    sorted_rides.remove(sorted_rides[r])
                    cont = False
                    asdf[c] += 1
            r += 1
print(asdf)
for a in range(0, F ):
    write_file.write(str(asdf[a]) + " ")
    for b in range(2, N+1):
        if b < len(matrix[a]):
            write_file.write(str(matrix[a][b].number) + " ")
    write_file.write("\n")

print(matrix)