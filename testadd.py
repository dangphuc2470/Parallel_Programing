toAdd = [0, 30, 150, 360]
paralePrefixSum = [0, 10, 30, 30, 70, 120, 60, 130, 210, 90, 190, 300]
chunksize = 3
toAdd_index = 0
i = 0
while i < len(paralePrefixSum):
    paralePrefixSum[i] += toAdd[toAdd_index]
    i = i + 1
    if i % 3 == 0:
        toAdd_index += 1
print(paralePrefixSum)
