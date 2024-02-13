numbers = [100, 24, 48, 2, "me", True, 15.5]

print(numbers[1])
print(numbers)

numbers.append(400)
print(numbers)

numbers.remove(2) ##degere gore
print(numbers)

numbers.pop(3) ##indexe gore siler, default son index
print(numbers)

##add = [70, 800, 900]
numbers.extend([1001133, 8071133, 901133])
print(numbers)

##numbers.clear()
##print(numbers)