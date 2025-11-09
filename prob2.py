#Find the minimum number of rabbits in a forest

def minrabbits(answers, N):
    
    #Initialize map
    map = {}
    
    #Traverse array and map arr[i] to the number of occurences
    for a in range(N):
        
        if answers[a] in map:
            map[answers[a]] += 1
        else:
            map[answers[a]] = 1
            
    #Initialize count as 0
    count = 0
    
    #Find the number groups and no. of rabbits in each group
    for a in map:
        
        x = a
        y = map[a]
        
        #Find number of groups and multiply them with number of rabbits in each group
        if (y % (x + 1) == 0):
            count = count + (y // (x + 1)) * (x + 1)
        else:
            count = count + (y // (x + 1) + 1) * (x + 1)
            
    #count gives minimum number of rabbits in the forest
    return count

arr = [2, 2, 0]
N = len(arr)

print(minrabbits(arr, N))