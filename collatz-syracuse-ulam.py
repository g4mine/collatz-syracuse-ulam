import platform, os
# Collatz-syracuse-ulam problem:
# Se o numero for par divida por dois
# se for impar, multiplique por tres e some um
# quando o numero chegar a "1", pare
# os 5 ultimos resultados sempre serao: 16, 8, 4, 2, 1
uos = platform.uname()[0]
if uos == 'Linux':
	os.system('clear')
elif uos == 'Windows':
	os.system('cls')
num = int(raw_input('Digite um numero: '))
i = 0
print '===> '+str(num)
while num > 1:
    if num %2 == 0:
        num /= 2
    else:
        num *= 3
        num +=1
    i += 1
    print str(i)+' ===> '+str(num)
