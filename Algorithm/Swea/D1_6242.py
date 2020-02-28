data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
bloodType = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}
for i in data:
        bloodType[i] += 1
print(bloodType)