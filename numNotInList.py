# Check whether any item from a list is in another list
# BSD Licensed

valuesToHunt = [
    795918,
    799529,
    797241,
    791816,
    797957,
    798050,
    ]
listToSearch = [
    793740,
    794349,
    795849,
    795254,
    794796,
    788725,
    793494,
    793733,
    ]

for i in valuesToHunt:
    if i in listToSearch:
        print('Found ' + str(i) + ' in the list.')
