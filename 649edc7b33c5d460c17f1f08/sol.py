"""Written by IDHM
64bit program 
"""
import sys
"""fastcall with rax and rcx I guess , using them to """
def codes(key:str):
    return key.encode("ascii")
         
def auth(key:list):
    return sum(map(lambda x: ( 13092 // x + 84675 ) * 799 +5  ,key[:8]),start=8)

if len(sys.argv) <= 1 : 
    sys.exit()

arg0 = sys.argv[1]
if len(arg0) < 8 : 
    print("WARNNING MIGHT NOT WORK !!!! ACCSSESING UNDEFINDED ALLOCATED MEMORY : EXTINING")
    sys.exit()
codes_gen = codes(arg0)
auth_gen = auth(codes_gen)
calc1 = (auth_gen * 0x66666667)
calc1 = (calc1 >> 0x21) 
calc2 = auth_gen > 2 ** 31 
calc3 = calc1 - calc2
calc4 = calc3 * 4 
calc5 = calc4 + calc3
res = auth_gen - calc5 #res is always 3 or 2 
print(f"res : {res} , key:{auth_gen}")
if res == 3 : 
    print("WIN")
else : 
    print("LOSE")