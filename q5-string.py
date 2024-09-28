text = input("digite uma sequencia de caracteres")
vector = list(text)
x = len(text)-1
for i in text:
  vector[x] = i
  x-=1
vector = "".join(vector)
print("A string invertida é: " + vector)

