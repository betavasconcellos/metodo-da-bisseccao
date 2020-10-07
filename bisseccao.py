import math

# definir intervalo e um erro
print('Método da Bissecção\nDefina o intervalo [a,b]')
a = float(input('Defina a: '))
b = float(input('Defina b: '))
erro = float(input('Defina a tolerância: '))
#num da iteração
it = 1
c=2
# constante e
e = 2.718281828459045235360287
#definir função
def f(x):
    return 4*x - e**x
    #return x*e**x-1

print('f(a)',f(a))
print('f(b)',f(b))

if f(a) > 0 and f(b) < 0:
    print('Existe raiz nesse intervalo!')
if f(a) < 0 and f(b) > 0:
    print('Existe raiz nesse intervalo!')

#iterações
if f(a)*f(b)<0:
    while(math.fabs(b-a)/c) > erro:
        c = (a + b) / 2  #teorema de bolzano

        print('A iteração {} resultou: {:.9f}'.format(it, c))
        if f(c) == 0:
            print('A raiz é {:.9f}'.format(c))
            break
        else:
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c

        print('f({}) = {}'.format(b,f(b)))
        print('f({}) = {}'.format(a,f(a)))
        it = it + 1
        print('Erro relativo', math.fabs(b-a)/c)
        if it > 20:
            break

    print('A raiz é: {:.9f}'.format(c))
else:
    print('Não há raiz neste intervalo!')
