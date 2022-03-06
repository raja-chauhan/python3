"""
r -> open for reading
w -> open for write
x -> if file exist than failed if not than work
a -> add more content to file at the end
t -> text mode (default mode)
b -> binary mode
+ -> open file for read and write mode


method used 
open() -> open file
read() -> read whole file
readline() -> read one line
"""

# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read()) or f.read(3) for 3 index only
# f.close()


"""
block to open file

with open ('dir) as f:
    a = f.read(4)
    print(a)


automatically close the file
"""