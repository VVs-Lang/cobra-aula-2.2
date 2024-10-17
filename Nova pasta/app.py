import random 

# Função que gera a introdução da ficha
def gerar_introducao():
    introducoes = ["Joao", "Maria", "Cleber"] 
    return random.choice(introducoes)

# Função que gera o desnvolvimento da ficha
def gerar_desenvolvimento():
    desenvolvimento = ["youtuber" , "taxi" , "padeiro" , "feiticeira",  "sábio mago"]
    return random.choice(desenvolvimento)

# Função que gera o final da ficha
def gera_final():
    finais = ["6 anos." , "12 anos." , "28 anos." , "90 anos." , "40 anos."]
    return random.choice(finais) 

# Funçaõ principal que gera toda a ficha
def gerar_ficha():
   introducao = gerar_introducao()
   desenvolvimento = gerar_desenvolvimento()
   final = gera_final()

   ficha= f" {introducao} {desenvolvimento} {final}"
   return ficha

#Exibe a historia gerada
if __name__ ==  "__main__":
    print(gerar_ficha())