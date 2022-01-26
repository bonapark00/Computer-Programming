
def a(n):
    lst = []
    if n == 1:
        return [1]

    else:
        lst += a(n-1)
        return lst

print(a(3))

# C:/Users/jp040/Downloads/
# C:/Users/jp040/OneDrive/Documents/연대 수업/컴프밍/sw교재


# print(searchDir('C:/Users/jp040/OneDrive/바탕 화면/alice_tea_party', 'jy'))






