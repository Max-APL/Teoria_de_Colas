class MM1():
    lamda = 0
    niuw = 0

    def __init__(self, lamda, niuw):
        self.__lamda = lamda
        self.__niuw = niuw

    # Getter
    @property
    def lamda(self):
        return self.__lamda

    # Setter
    @lamda.setter
    def lamda(self,valor):
        self.__lamda = valor

    # Getter
    @property
    def niuw(self):
        return self.__niuw

    # Setter
    @niuw.setter
    def niuw(self,valor):
        self.__niuw = valor

    # Funciones
    def p0(self):
        return 1-self.p()

    def Lq (self):          
        temp1=(self.__lamda**2)
        temp2=(self.__niuw*(self.__niuw-self.__lamda))
        total=temp1/temp2
        return total

    def Ls(self):
        total=(self.__lamda/(self.__niuw-self.__lamda))
        return total

    def Wq(self):
        temp=(self.__niuw*(self.__niuw-self.__lamda))
        total= self.__lamda/temp
        return total

    def Ws(self):
        total= 1/(self.__niuw-self.__lamda)
        return total

    def Pn (self,n):
        total = (1-self.p()) * pow(self.p(),n)
        return total
    
    def p(self):
        return (self.__lamda/(self.__niuw*1))


#self.__s = int(input("Bienvenido a el Sistema M/M/s  por favor ingrese cuantos self.ses va a usar:\n  "))

#self.__lamda = int(input("Ingrese la tasa media de llegada de la Empresa(λ):\n "))

#self.__niuw = int (input("Ingrese la tasa media de servivio (μ):\n  "))
#p=(self.lamda/(self.niuw*self.s))
'''
print ("el ro (ρ) es;",p)
print("La probabilidad de que el sistema este vacio es de:",p0(self.lamda,self.niuw,self.s))
print("La longitud de la cola es de:   ",Lq(self.lamda,self.niuw,self.s))
print("La longitud en el sitema es de:   ",Ls(self.lamda,self.niuw,self.s))
print("El tiempo de espera promedio en cola es de :   ",Wq(self.lamda,self.niuw,self.s))
print("El tiempo de espera promedio en el sistema es de :   ",Ws(self.lamda,self.niuw,self.s))
Cn(self.lamda,self.niuw,self.s)

'''
modeloMMS = MM1(10,15)

print("1: ", modeloMMS.p())
print("2: ", modeloMMS.p0())
print("3: ", modeloMMS.Lq())
print("4: ", modeloMMS.Ls())
print("5: ", modeloMMS.Wq())
print("6: ", modeloMMS.Ws())
print("7: ", modeloMMS.Pn(10))





