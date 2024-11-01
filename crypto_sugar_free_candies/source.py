from Crypto.Util.number import bytes_to_long,long_to_bytes

# FLAG = open("flag.txt", "rb").read()

# step = len(FLAG) // 3
# candies = [bytes_to_long(FLAG[i:i+step]) for i in range(0, len(FLAG), step)]

# cnd1, cnd2, cnd3 = candies

# with open('output.txt', 'w') as f:
#     f.write(f'v1 = {cnd1**3 + cnd3**2 + cnd2}\n')
#     f.write(f'v2 = {cnd2**3 + cnd1**2 + cnd3}\n')
#     f.write(f'v3 = {cnd3**3 + cnd2**2 + cnd1}\n')
#     f.write(f'v4 = {cnd1 + cnd2 + cnd3}\n')
s=[{"cnd1": 1612993708938936929835517754497931126786454632, "cnd2": 2260690199455691264676123410341531247524997487, "cnd3": 2463132351713367737738737327711828586109296509}]
s1=''
for i in s[0].keys():


    s1+=str(long_to_bytes(s[0][i]))
print(s1)
# HTB{__protecting_the_secret_in_equations_is_not_secure__}