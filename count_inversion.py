def count_inversion(sequence):
    counter = 0;
    for i in range(0, len(sequence) - 1):
        if sequence[i] > sequence[i+1]:
            for j in range(i, len(sequence)):
                if sequence[i] > sequence[j]:
                    counter = counter + 1
                
    return counter

print count_inversion((5,3,2,1,0))
