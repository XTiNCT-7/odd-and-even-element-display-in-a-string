T = int(input("Enter no. of Test cases"))
for line in range(T):
    s = input("enter string")
    even_string = ""
    odd_string = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_string = even_string + s[i]
        else:
            odd_string = odd_string + s[i]
    print(even_string, odd_string)
