# -*- coding: utf-8 -*-
#Autora: Camila Andrea Miguras Prado
#Fecha: 09 de diciembre, 2024
#Asignatura: Funciones y Progresiones

#Funciones
def Real(a,b): #Tasa de interés real
    r = float(f'{(((1+a/100)/(1+(b/100))-1)*100):.4f}')
    return r
def TransTasasMayorMenor(a,b): #Tasa mayor a menor periodo de capitalización
    t = float(f'{((((1+(a/100))**(1/b))-1)*100):.2f}')
    return t
def TransTasasMenorMayor(a,b): #Tasa menor a mayor periodo de capitalización
    t = float(f'{((((1+(a/100))**b)-1)*100):.2f}')
    return t
def MontoInflacion(a,b,c): #Valor futuro para inflación
    m = int(a/((1+b/100)**c))
    return m
def MontoFuturo(a,b,c): #Función de Valor Futuro
    m = int(a*((1+b/100)**c))
    return m

#Datos
IPC = float(f'{4.1/12:.2f}')
Bancos = ["1. Banco de Chile","2. Internacional","3. Banco Estado de Chile","4. Scotiabank","5. BCI","6. Bice","7. Hsbc Bank", "8. Santander","9. Security","10. Falabella","11. Ripley","12. Consorcio","13. BTG Pactual","14. China Construction Bank","15. Banco Itaú Chile"]
D30 = [float(5.11),float(6.34),float(4.93),float(5.54),float(5.20),float(5.37),float(4.74),float(4.35),float(5.66),float(5.04),float(6.24),float(5.98),float(5.95),float(5.41),float(5.59)]
D60 = [float(5.20),float(6.35),float(5),float(5.39),float(5.42),float(5.35),0,float(4.94),float(5.65),float(5.17),float(6.18),float(5.97),float(5.98),0,float(5.56)]
D90 = [float(5.25),float(5.77),float(4.95),float(5.13),float(5.33),float(5.34),float(5.67),float(4.95),float(5.64),float(5.02),float(5.81),float(5.74),float(5.78),float(5.48),float(5.64)]
#Convertidor de tasas anuales
for i in range(len(D30)):
    D30[i] = TransTasasMayorMenor(D30[i], 12)
for i in range(len(D60)):
    D60[i] = TransTasasMayorMenor(D60[i], 6)
for i in range(len(D90)):
    D90[i] = TransTasasMayorMenor(D90[i], 4)
#Título
print("TASAS DE INTERÉS")
print("Período Septiembre 2024")
print("Variación IPC promedio mensual últimos 12 meses a la fecha: ", IPC,"%")
print("")
#Definición de periodos de capitalización
cap = int(input("Ingrese días de depósito a plazo: "))
if ((cap != 30) and (cap != 60) and (cap != 90)):
    while (cap != 30 and cap != 60 and cap != 90):
        cap = int(input("Vuelva a ingresar los días de depósito: "))
print("")
#Transformación tasa de inflación en caso de periodos distintos a 30 días
if cap == 60:
    IPC = TransTasasMenorMayor(IPC, 2)
elif cap == 90:
    IPC = TransTasasMenorMayor(IPC, 3)
#Selección de banco
con = 0
while(con < 15):
    if cap == 30:
        print(Bancos[con]," = ",D30[con],"%")
    elif cap == 60:
        print(Bancos[con]," = ",D60[con],"%")
    elif cap == 90:
        print(Bancos[con]," = ",D90[con],"%")
    con = con + 1   
print("")
OpBco = int(input("Escriba el número de la opción: ")) - 1
print("")
#Definicion tasa de interés nominal
if cap == 30:
    IntN = (D30[OpBco])
elif cap == 60:
    IntN = (D60[OpBco])
elif cap == 90:
    IntN = (D90[OpBco])
#Definicion tasa real
IntR = Real(IntN,IPC)
print("Tasa real: ",IntR,"%")
print("")
#Definición monto y periodos
MonInicial = int(input("Ingrese monto a invertir: "))
print("")
Periodo = int(input("Ingrese período a visualizar: "))
print("")
#Proyecciones al usuario
MonInflacion = MontoInflacion(MonInicial, IPC, Periodo)
MonNominal = MontoFuturo(MonInicial, IntN, Periodo)
MonReal = MontoFuturo(MonInicial, IntR, Periodo)
print("Valores reales del monto inicial al periodo ingresado: $",MonInflacion, "( -$",int(MonInicial-MonInflacion),")")
print("Valores nominales del monto futuro: $",MonNominal,"( +$",int(MonNominal-MonInicial),")")
print("Valores reales del monto futuro: $",MonReal,"( +$",int(MonReal-MonInicial),")")