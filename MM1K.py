
class MM1K():
    lamda = 0
    niuw = 0
    k = 0

    def __init__(self, lamda, niuw, k):
        self.__lamda = lamda
        self.__niuw = niuw
        self.__k = k

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

    # Getter
    @property
    def k(self):
        return self.__k

    # Setter
    @k.setter
    def s(self,valor):
        self.__k = valor

    # Funciones

    def p(self):
        return (self.__lamda/(self.__niuw*1))
    
    def p0(self):
        total = (1-self.p())/(1-(pow(self.p(),self.__k+1)))
        return total

    def Pn (self,n):
        total = (1-self.p())/(1-(pow(self.p(),self.__k+1)))
        return total * pow(self.p(),n)
    
    def Lq (self):

        total= self.Ls()-(1-self.p0())
        return total

    def Ls(self):
        temp1 = (self.p()) / (1-self.p())
        temp2 = ((self.__k+1)*pow(self.p(),(self.__k+1))) / (1-pow(self.p(),(self.__k+1)))
        return temp1 - temp2

    def lam_prom(self):
        return self.__lamda*(1-self.Pn(self.__k))
    
    def Wq(self):
        total= self.Lq()/self.lam_prom()
        return total

    def Ws(self):
        total = self.Ls()/self.lam_prom()
        return total

    
        
    


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
modeloMMS = MM1K(5,10,4)

print("1: ", modeloMMS.p())
print("2: ", modeloMMS.p0())
print("3: ", modeloMMS.Lq())
print("4: ", modeloMMS.Ls())
print("5: ", modeloMMS.Wq())
print("6: ", modeloMMS.Ws())
print("7: ", modeloMMS.Pn(4))






