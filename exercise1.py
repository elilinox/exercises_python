def cagr_berechnung(AK,t,EK):
        cagr = (((EK/AK)**(1/t))-1)*100
        AK = abs(AK)
        EK = abs(EK)
        t = abs(t)
        return cagr
x = cagr_berechnung(100, 30, 700)
print(x)

AK=120
t=30
EK_2 = AK* (1+ x/100)**t

print(EK_2)