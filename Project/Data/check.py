import json

data = open('data.json', 'r')

data = json.load(data)
state_names_list = list()
state_names_set = set()


# for i in range(3721, 3779):
#     data['records'][i] = 0

# for i in range(3370, 3370):
#     data['records'][i] = 0

# for i in range(2785, 2843):
#     data['records'][i] = 0

# for i in range(2902, 2960):
#     data['records'][i] = 0

# for i in range(328, 386):
#     data['records'][i] = 0

# for i in range(3604, 3662):
#     data['records'][i] = 0


for values in data['records']:
    # if(values['subdivision'] == 'East Uttar Pradesh'):
    #     print(values['subdivision'])
    #     print(data['records'].index(values))
    #     data['records'].pop(data['records'].index(values))

    state_names_set.add(values['subdivision'])

# print(state_names_set)
for i in state_names_set:
    state_names_list.append(i)


state_names_list.sort()
for state in state_names_list:
    print(state)
