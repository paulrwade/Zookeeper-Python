number = int(input())
word = str(input())

result = str(number) + " " + word

if number == 0 or number > 1:
    result = result + "s"

print(result)
