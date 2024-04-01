n1 = float(input("Insira a primeira nota:"))
n2 = float(input("Insira a segunda nota:"))

m = (n1 + n2) / 2

if 9 < m <= 10:
    print("O aluno foi aprovado com nota A, e uma média de", m)

elif 7.5 < m <= 8.9:
    print("O aluno foi aprovado com nota B, e uma média de", m)

elif 6 < m <= 7.4:
    print("O aluno foi aprovado com nota C, e uma média de", m)
    
elif 4 < m <= 5.9:
    print("O aluno foi reprovado com nota D, e uma média de", m)
    
elif 0 <= m <= 3.9:
    print("O aluno foi reprovado com nota E, e uma média de", m)
