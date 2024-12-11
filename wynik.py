import onp
import insert

# wynik = 0
# i = 0
# dzialania = {'+','-','*','/','^'}
# while len(onp) > 1:
#     if onp[i] in dzialania:
#         if onp[i] =='+':
#             onp[i-2]+=onp[i-1]
#         elif onp[i] =='-':
#             onp[i-2]-=onp[i-1]
#         elif onp[i] =='*':
#             onp[i-2]*=onp[i-1]
#         elif onp[i] =='/':
#             onp[i-2]/=onp[i-1]
#         onp.pop(i)
#         onp.pop(i - 1)
#         i-=2
#     i+=1
print(onp.onp(insert.expression()))