word = str(input("Digite a frase a ser analisada: "))
letter = str(input("Informe a letra que deseja consultar a quantidade "))

final_result = word.count(letter)

if letter in word:
  print(f'há {final_result} ocorrência(s) dessa letra')
else:
  print("Não há essa letra")

