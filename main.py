print("Hi World")

##degiskenler
#metinsel, numerik, obje

text = "hallo"
user_name = "hanifay"
print(text + ' ' + user_name)

studentCount = "45" ##string
print(studentCount + "5")

studentCount = 45 ##numeric
print(studentCount + 5)

avaragePoint = 25.5 # double float decimal
print(avaragePoint + 5)

isVerified = True #boolen
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(avaragePoint))
print(type(isVerified))

#matematiksel mantıksal
number = 10
print(10 + 10)
print(number + number)

print(number-5)

print(number / 3)

print(number * 3)

print(number % 3) #mod

##matiksal operatorler => karsilastirma operatorleri

print(number == 10) #true
print(number == 11) #false

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

##string interpolation -> metin birlestirme
text = "hallo"
userName = "hanifay"
totalText = text + ' ' + userName
print(totalText)

totalText = "{message} Mrs. {name}".format(message=text, name=userName)
print(totalText)

##f-string
totalText = f"Welcome {userName}"
print(type(totalText))

