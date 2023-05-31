class Ordenacao():

    def __init__(self, array_para_ordenar:list):
        self.__array_para_ordenar=array_para_ordenar

    def ordena(self):

        for i in range(len(self.__array_para_ordenar)):
            for i in range(1,len(self.__array_para_ordenar)):
                if self.__array_para_ordenar[i-1]>self.__array_para_ordenar[i]:
                    self.__array_para_ordenar[i], self.__array_para_ordenar[i-1]=self.__array_para_ordenar[i-1],self.__array_para_ordenar[i]
        return self.array_para_ordenar

    def toString(self):
        nova_lista=[]
        for i in self.__array_para_ordenar:
            nova_lista.append(str(i))
        return ','.join(nova_lista)

        # string=''
        # for i in range(len(self.array_para_ordenar)):
        #     self.array_para_ordenar[i]=str(self.array_para_ordenar[i])
        #     if i!=(len(self.array_para_ordenar)-1):
        #         string+=f'{self.array_para_ordenar[i]},'
        #     else:
        #         string+=self.array_para_ordenar[i]
       
        # return string

    
    @property
    def array_para_ordenar(self):
        return self.__array_para_ordenar
    
    @array_para_ordenar.setter
    def array_para_ordenar(self, array_para_ordenar):
        self.__array_para_ordenar=array_para_ordenar

if __name__=='__main__':
    o=Ordenacao([5,3,2,1,4])
    o.ordena()
    print(o.toString())