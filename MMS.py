
class MMS():
    lamda = 0
    niuw = 0
    s = 0

    def __init__(self, lamda, niuw, s):
        self.__lamda = lamda
        self.__niuw = niuw
        self.__s = s

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
    def s(self):
        return self.__s

    # Setter
    @s.setter
    def s(self,valor):
        self.__s = valor

    # Funciones
    def p0(self):
        suma=0
        suma2=0
        multi=0
        total=0
        for i in range(0, self.__s):
            suma= suma+((pow((self.__lamda/self.__niuw),i))/self.factorial(i))
        
        suma2=((pow((self.__lamda/self.__niuw),self.__s))/self.factorial(self.__s))
    
        multi=1/(1-(self.__lamda/(self.__niuw*self.__s)))
        
        total=1/(suma+suma2*multi)
        
        return total

    def factorial(self, numero):
        if numero == 0:
            return 1
        else:
            return numero * self.factorial(numero-1)


    def Lq (self):
        
        p=(self.__lamda/(self.__niuw*self.__s))
        
        temp1=(self.p0()*(pow(self.__lamda/self.__niuw,self.__s)*p))
        temp2=(self.factorial(self.__s)*(pow(1-p,2)))
        total=temp1/temp2
        return total

    def Ls(self):
        total=(self.Lq()+(self.__lamda/self.__niuw))
        return total

    def Wq(self):
        total=self.Lq()/self.__lamda
        return total

    def Ws(self):
        total =self.Wq()+(1/self.__niuw)
        return total

    def Pn (self,n):
        if (n<=self.__s):
            total=((pow(self.__lamda/self.__niuw,n)/self.factorial(n)))*self.p0()
            return total
        else:
            total= (((pow((self.__lamda/self.__niuw),n) )/(self.factorial(self.__s)*  pow(self.__s,(n-self.__s)))))*self.p0()
            return total
    
    def p(self):
        return (self.__lamda/(self.__niuw*self.__s))


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
modeloMMS = MMS(120,80,10)

print("1: ", modeloMMS.p())
print("2: ", modeloMMS.p0())
print("3: ", modeloMMS.Lq())
print("4: ", modeloMMS.Ls())
print("5: ", modeloMMS.Wq())
print("6: ", modeloMMS.Ws())
print("7: ", modeloMMS.Pn(5))






