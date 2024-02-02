c_temp = input()
c_lst = [float(temp) for temp in c_temp.split()]

f_lst = [round((celsius * 9 / 5) + 32) for celsius in c_lst]

for f in f_lst:
    print(f)
