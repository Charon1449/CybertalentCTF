from itertools import permutations
import base64
arr = ["zg5" ,"zND" ,"MTI" ,"U2N"]

perm = list(permutations(arr))
#MAo=

for permutation in perm :
    possible_flag = "".join(permutation)+"MAo="
    print(base64.b64decode(possible_flag))
