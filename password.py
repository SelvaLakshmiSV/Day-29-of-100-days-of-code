import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) 
number=chr(random.randint(48,57))
uppercaseLetter3=chr(random.randint(65,90))
lowercaseLetter4=chr(random.randint(97,122))
uppercaseLetter5=chr(random.randint(65,90))
uppercaseLetter6=chr(random.randint(65,90))
lowercaseLetter7=chr(random.randint(97,122))
uppercaseLetter8=chr(random.randint(65,90))
lowercaseLetter9=chr(random.randint(97,122))
specialLetter10=chr(random.randint(35,38))
uppercaseLetter11=chr(random.randint(65,90))
lowercaseLetter12=chr(random.randint(97,122))

password = uppercaseLetter1 + number + uppercaseLetter3 + lowercaseLetter4 + uppercaseLetter5 +uppercaseLetter6 + lowercaseLetter7 +uppercaseLetter8 +lowercaseLetter9 +specialLetter10 +uppercaseLetter11 +lowercaseLetter12        
password = shuffle(password)


print(password)
