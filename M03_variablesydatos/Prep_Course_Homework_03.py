#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

variable = 4
print(variable)





# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

type(8.5)





# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(variable)




# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre = 'Anuark Jimenez'



# 5) Crear una variable que contenga un número complejo

# In[3]:

num_comple = 4+5j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(num_comple)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

variablel1 = 'True'
variable2 = True

variablel1 == variable2



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# In[5]:

print('La variable variable11 es de tipo', type(variablel1), ' y la variable2 es de tipo', type(variable2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 56 + 5.6



# 11) Realizar una operación de suma de números complejos

# In[2]:

num1 = 4 + 7j
num2 = 34 + 98j

print(num1 + num2)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

sumcom = 45 + 4j
sumRe = 67
print(sumcom + sumRe)



# 13) Realizar una operación de multiplicación

# In[5]:


print(4 * 7)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

cociente = 27/4
print(cociente)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

p_entera = 27 // 4
print(p_entera)





# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

resto = 27 % 4
print(resto)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print(4 * p_entera + resto)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

nombre = 'Anuark '
apellido = 'Jimenez'

nombre + apellido




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

"2" == 2



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int("2") == 2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3,8')




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

y = 3
y -= 1
print(y)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


2 + int('2')




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

jaa = 'Ja! '
veces = 4

print(jaa * veces)
