from hash_map import Dict
class Bharath:
    def __init__(self, value):
        self.value  = value

if __name__ == '__main__':
#     a = 5*[None]
#     print(a)
#
#     a[2] = ([Dict(2,3)])
#     a[2].append(Dict(3,3))
#
#
#     k, v = a[2][0].get_item()
#
#
#     for pair in a[2]:
#
#         pair.value = 4
#
#
# print(a[2][0].get_item())
# print(a[2][1].get_item())



    a = [[1,2], [2,3]]

    for i in a:

        i[0] = 0
        i[1] = 0
        print("i", i)

