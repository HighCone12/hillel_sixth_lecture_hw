d = {'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}},'id3':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}}}
new_d = {}
[new_d.update({k: v})
 for k, v in d.items()
    if v not in new_d.values()]
print(new_d)