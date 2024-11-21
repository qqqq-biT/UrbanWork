grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

s = sorted(list(students))

g = (float(sum(grades[0])) / (len(grades[0])))
g_1 = (float(sum(grades[1])) / (len(grades[1])))
g_2 = (float(sum(grades[2])) / (len(grades[2])))
g_3 = (float(sum(grades[3])) / (len(grades[3])))
g_4 = (float(sum(grades[4])) / (len(grades[4])))

a = {g: s[0], s[1]: g_1, s[2]: g_2, s[3]: g_3, s[4]: g_4}
print(a)
