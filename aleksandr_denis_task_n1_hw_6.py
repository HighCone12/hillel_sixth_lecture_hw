first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
for key,value in first.items():
    second[key] = value
second.update(third)
sixth = {**second, **fourth, **fifth}
print(sixth)

