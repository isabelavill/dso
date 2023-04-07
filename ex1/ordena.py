class Ordenacao(): 

    def __init__(self, array_para_ordenar:list):
        self.array_para_ordenar=array_para_ordenar
        

    def ordena(self):
        for i in range(len(self.array_para_ordenar)):
           for i in range(1, len(self.array_para_ordenar)):
                if self.array_para_ordenar[i-1]>self.array_para_ordenar[i]:
                    self.array_para_ordenar[i], self.array_para_ordenar[i-1] = self.array_para_ordenar[i-1], self.array_para_ordenar[i]
        
        return self.array_para_ordenar
        
    def toString(self):
        string=''
        for i in range(len(self.array_para_ordenar)):
            self.array_para_ordenar[i]=str(self.array_para_ordenar[i])
            if i!=(len(self.array_para_ordenar)-1):
                string+=f'{self.array_para_ordenar[i]},'
            else:
                string+=self.array_para_ordenar[i]
       
        return string


lista=Ordenacao([])
lista.ordena()
