import package_calculando.calculos_basicos

x = int(input("Digite um numero: "))

y = int(input ("Digite mais um : "))


calculo1 = package_calculando.calculos_basicos.sub_numbers (x , y)
print(f"A substração dos valores informados é: {calculo1}")

calculo2 = package_calculando.calculos_basicos.add_numbers (x , y)
print(f"A soma dos valores informados é: {calculo2}")

calculo3 = package_calculando.calculos_basicos.mult_numbers (x , y)
print(f"A multiplição dos valores informados é: {calculo3}")

calculo4 = package_calculando.calculos_basicos.div_numbers (x , y)
print(f"A divisão dos valores informados é: {calculo4}")