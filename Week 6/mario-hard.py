a = int(input())

while a < 0 or a > 8:
    a = int(input())

for i in range (1, a):
    spaces = a - i - 1
    hashnums = i * "#"
    print(" " * spaces + hashnums + " " + hashnums)
