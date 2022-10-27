# **************************************************************************** #
#                turn no space to have space                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Jayz <Jayzyzy@outlook.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/05 17:14:48 by Jayz              #+#    #+#              #
#    Updated: 2022/10/05 17:14:48 by Jayz             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# NOSPACENB = input('NSPB')
NOSPACENB = "1067919119678511269369181156920948"
NSPBLIST = []
# for i in range(len(NOSPACENB)//3):
#     try: 
#         NSPBLIST.append(int(NOSPACENB[3*i:3*(i+1)]))
#     except:
#         break
# print(NSPBLIST)
while len(NOSPACENB) > 3:
    if int(NOSPACENB[0:3]) > 700 : 
        NSPBLIST.append(int(NOSPACENB[0:3]))
        NOSPACENB = NOSPACENB[3:]
    else : 
        NSPBLIST.append(int(NOSPACENB[0:4]))
        NOSPACENB = NOSPACENB[4:]

print(NSPBLIST)

