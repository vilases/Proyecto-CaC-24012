lista=[1,1,4,7,5,9,7,5,8,4,9,2,5,4,6,4,9,1,2,1]

def moda(lista,nulos=True):
    #Obtenemos los valores unicos de la lista
    unicos= set(lista)

    l_unicos=[]

    for item in unicos:
        l_unicos.append(item)

    
    #Crramos una lista de "tuplas" con un valor y una frecuencia. Se pueden contar los nulos o no 
    tuplas=[]
    for item in l_unicos:
        if nulos==True:
            if item!=None and item!='':
                tuplas.append([item,0])
        else:
            tuplas.append([item,0])
    
    #Se comparan los valorrs de ambas listas y se incrementan las frecuencias  
    for item in lista:
        for it in tuplas:
            if item==it[0]:
                it[1]+=1
   
    #Creamos la lista moda con 2 valores: una lista con las modas y la frecuencia. 
    moda=[[],0]
    
    #Se recorren los items de "tuplas". Si la frecuencia es mayor a la de "moda" esta toma sus valores. Si es igual se agrega el valor a la lista de valores
    for item in tuplas:
        if item[1]>moda[1]:
            moda[0]=[item[0]]
            moda[1]=item[1]
        elif item[1]==moda[1]:
            moda[0].append(item[0])
          
    moda[0]=tuple(moda[0])
    moda=tuple(moda)
    return moda
    

def media(lista):
    tupla=[]
    media=0
    for item in lista:
        
        if item!=None and item!='':
                tupla.append(item)
    
    for item in tupla:
        media +=float(item)
    
    media/=len(tupla)
    return  round(media,2)

def min(lista):
    tupla=[]
    for item in lista:
        
        if item!=None and item!='':
                tupla.append(item)
    min=tupla[0]
    
    for item in tupla:
        if item < min:
            min=item
    return min

def max(lista):
    tupla=[]
    for item in lista:
        
        if item!=None and item!='':
                tupla.append(item)
    max=tupla[0]
    
    for item in tupla:
        if item > max:
            max=item
    return max

def mediana(lista):
    l_ord=sorted(lista)
    
    largo=len(l_ord)
    if len(l_ord)%2==0:
        mediana=(l_ord[int(largo/2)]+l_ord[int(largo/2+1)])/2
    else:
        mediana = l_ord[int((largo/2)+0.5)]
    return mediana
    
def dst(lista):
    list=[]
    for item in lista:
        
        if item=='' or item==None:
            list.append(0)
        else:
            list.append(float(item))
   
    med=media(list)
    sum=0
    for item in  list:
        sum+=(float(item)-med)**2
    return (sum/len(list))**(1/2)
    
def rango(lista):
    return max(lista)-min(lista)

def quartil(lista,num=1):
     lista=sorted(lista)
     l_ord=[]
     for item in lista:
         l_ord.append(float(item))
     
     q=num*(len(l_ord)+1)/4
     
     if round(q)==q:
        
         return l_ord[int(q)]
         
     else:
         
         return l_ord[round(q)]+(q-round(q))*(l_ord[round(q)+1]-l_ord[round(q)])

    
    
print (max(lista))
print (min(lista))
print (media(lista))
print(mediana(lista))      
print(dst(lista))
print (rango(lista))
print(quartil(lista,1))
print(quartil(lista,2))
print(quartil(lista,3))