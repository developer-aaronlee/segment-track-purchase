"""Convert two lists into a dictionary"""

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

"""Method 1"""
# dic1 = {}
# for key in test_keys:
#     for value in test_values:
#         dic1[key] = value
#         test_values.remove(value)
#         break
#
# print(dic1)

"""Method 2"""
# dic2 = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
#
# print(dic2)

"""Method 3"""
dic3 = dict(zip(test_keys, test_values))

print(dic3)
