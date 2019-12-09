# Mendel's First Law

k = 28  # homozygous (AA)
m = 21  # heterozygous (Aa)
n = 20  # homozygous recessive (aa)

AL = 2*(k + m + n)
AL1 = AL-1

A = k*2 + m
a = n*2 + m

pA_1 = A/AL
pa_1 = a/AL

#outA2 = (A-1)/(A+a-1)*a_1 + (a)/(A+a-1)*A_1 + (A)/(A+a-1)*a_1
outA22 = 1-(a-1)/AL1*pa_1

#print(outA2)
print(outA22)



