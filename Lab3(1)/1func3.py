def solve(numheads,numlegs):
    for i in range(numheads):
        for j in range(numheads):
            if (i*4)+(j*2) == numlegs:
                if (i+j) == numheads:
                    print("Rabbits: " + str(i) + " " + "Chickens: " + str(j))
                else:
                    continue


numheads = 35
numlegs = 94
solve(numheads,numlegs)