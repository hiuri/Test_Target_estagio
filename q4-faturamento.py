faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = 0
for i in faturamento:
  total+= faturamento[i]
for i in faturamento:
  print("o percentual do estado " + i + " foi " + str((faturamento[i]/total)*100))

