def is_primo(numero):
    temp_numero = numero
    while(temp_numero>0):
        if(temp_numero!=numero and temp_numero!=1):
            if (numero%temp_numero==0):
                return False
        temp_numero-=1
    return True 

def get_next_primo(current):
    temp_numero= current+1
    while True:
        if(is_primo(temp_numero)):
            return temp_numero
            break
        temp_numero +=1

def primos(numero):
    result = []
    last_primo = 0
    for num in range(numero):
        last_primo = get_next_primo(last_primo)
        result.append(last_primo)
    return result

if __name__ == "__main__":
    primos_n = primos(10)
    print(primos_n)

        