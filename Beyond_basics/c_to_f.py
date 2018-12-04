temperatures = [10, -20 , -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make any sense!"
    else:
        f = c* 9/5 +32
        return f
# for t in temperatures:
#     print(c_to_f(t))

with open("c_to_f.txt","w") as myfile:
    for t in temperatures:
        if t >= -273.15:
            myfile.write(str(c_to_f(t))+ "\n")
