from operator import itemgetter

my_diction = {"ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1}
max_capacity_backpack = 1.0
weight = 0
capacity_backpack = 0

for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
    weight += my_diction[things]

    if weight <= max_capacity_backpack:
        capacity_backpack += my_diction[things]

print("Все возможные варианты наполнгения рюкзака при допустимой грузоподьемности в ", max_capacity_backpack, "кг")

list_dict_value = []
list_dict_key = []
for key, value in my_diction.items():
    list_dict_key.append(key)
    list_dict_value.append(value)

def subset_sum(weights, things, target, count, partial_weights=[], partial_things=[]):
    s = sum(partial_weights)

    if s <= target:
        print("список вещей(%s)\nвес вещей(%s) <= %s \n" % (partial_things, partial_weights, target))

    if s >= target:
        return  

    for i in range(len(weights)):
        n = weights[i]
        remaining_weights = weights[i + 1:]
        m = things[i]
        remaining_things = things[i + 1:]
        subset_sum(remaining_weights, remaining_things, target, count + 1, partial_weights + [n], partial_things + [m])

print(subset_sum(list_dict_value, list_dict_key, max_capacity_backpack, 0))