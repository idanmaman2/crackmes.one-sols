from itertools import combinations
import string
def auth(key:list):
    return sum(map(lambda x: ( 13092 // x + 84675 ) * 799 +5  ,key[:8]),start=8)
def good(authkey : str): 
    def verfiy (key:int):
        return (key -  (((key * 0x66666667) >> 0x21) - (key > 2 ** 31)) * 5 ) == 3 
    return verfiy(auth(authkey.encode("ascii")))
counter = 0 
with open("all_answers.txt" , 'w') as file:
    for answer in filter(lambda x :good(x) , map(lambda x : "".join(x) , combinations(string.ascii_letters + string.digits ,r=8 ))  ): 
        file.write(f"{str(counter:=counter+1)}.) {answer}\n")