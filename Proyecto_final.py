#################################################################### F U N C I O N E S #############################################################################
def preguntasmate1(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    if numero_pregunta==1:
        print('PREGUNTA MATEMÁTICAS 1')
        print ('''¿A cuánto equivale pi?
Escriba la letra del inciso de su respuesta.

    A) 3.578
    B) 2.46
    C) 3.1416
    D) 4.1316''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='C':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasmate1(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==3:
        print('PREGUNTA MATEMÁTICAS 2')
        print('¿Cuál es la respuesta de la siguiente operación (40/5+18/3-1)?')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='13':
            puntos+=100
            print('\nCORRECTO')
        elif resp.isdecimal():
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE UN VALOR NUMÉRICO\n')
            puntos=preguntasmate1(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==5:
        print('PREGUNTA MATEMÁTICAS 3')
        print('''
 En el colegio de Irene, su profesora de ciencias les hace exámenes que se puntúan de 0 a 100. Irene tiene
 una media de 60 puntos de sus primeros cuatro exámenes de ciencias. En el quinto examen sacó 80 puntos. 

¿Cuál es la media de las notas de Irene en ciencias después de los cinco exámenes? ''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='64':
            puntos+=100
            print('\nCORRECTO')
        elif resp.isdecimal():
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE UN VALOR NUMÉRICO\n')
            puntos=preguntasmate1(numero_pregunta)
        
        return puntos
    
    else:
        return puntos
    
def preguntasmate2(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    if numero_pregunta==2:
        print('PREGUNTA MATEMÁTICAS 1')
        print('''¿Cuál es la raíz cuadrada de 64?
Escriba la letra del inciso de su respuesta.

    A) 7
    B) 8
    C) 6
    D) 4''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='B':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasmate2(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==4:
        print('PREGUNTA MATEMÁTICAS 2')
        print('''En una pizzería se puede elegir una pizza básica con dos ingredientes: queso y tomate. También
puedes diseñar tu propia pizza con ingredientes adicionales. Se pueden seleccionar entre cuatro ingredientes adicionales
diferentes: aceitunas, jamón, champiñones y salami. 
Jaime quiere encargar una pizza con dos ingredientes adicionales diferentes. 

¿Cuántas combinanciones puede hacer Jaime?''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='6':
            puntos+=100
            print('\nCORRECTO')
        elif resp.isdecimal():
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE UN VALOR NUMÉRICO\n')
            puntos=preguntasmate2(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==6:
        print('PREGUNTA MATEMÁTICAS 3')
        print('''¿Cuál es la estatura media de los siguientes alumnos: Juan-160cm, Regina-170, Pedro-150cm, Caro-180cm, Ricky-140cm?
Escriba la letra del inciso de su respuesta.

    A) 165cm
    B) 155cm
    C) 150cm
    D) 160cm''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='D':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasmate2(numero_pregunta)
        
        return puntos
    
    else:
        return puntos
#####################################################################################################################################################################
def preguntasciencias1(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    if numero_pregunta==7:
        print('PREGUNTA CIENCIAS 1') #geologia
        print('''¿Qué frase explica porqué hay día y noche en la Tierra?
Escriba la letra del inciso de su respuesta.

    A) El eje de la Tierra está inclinado
    B) El Sol gira alrededor de su eje
    C) La Tierra gira alrededor de su eje
    D) La Tierra gira alrededor del Sol''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='C':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasciencias1(numero_pregunta)
        
        return puntos

    elif numero_pregunta==9:
        resps=[]
        print('PREGUNTA CIENCIAS 2') #quimica
        print('''\tUn cocinero hace el pan mezclando harina, agua, sal y levadura. Una vez
    mezclado todo, coloca la mezcla en un recipiente durante varias horas para que se
    produzca el proceso de fermentación. Durante la fermentación, se produce un cambio
    químico en la mezcla: la levadura (un hongo unicelular) transforma el almidón y los
    azúcares de la harina en dióxido de carbono y alcohol. ¿De dónde provienen los átomos
    de carbono que forman parte del dióxido de carbono y de alcohol?
    
    Responda V si el enunciado es verdadero y F si el enunciado es falso.''')

        respuesta1=input('Algunos átomos de carbono provienen de los azúcares: ')
        respuesta1=respuesta1.upper()
        resps = resps + [respuesta1]
        respuesta2=input('Algunos átomos de carbono formaban parte de las moléculas de sal: ')
        respuesta2=respuesta2.upper()
        resps = resps + [respuesta2]
        respuesta3=input('Algunos átomos de carbono provienen del agua: ')
        respuesta3=respuesta3.upper()
        resps = resps + [respuesta3]
        respuesta4=input('Los átomos de carbono se formaron a partir de otros elementos en una reacción química: ')
        respuesta4=respuesta4.upper()
        resps = resps + [respuesta4]
        
        for i in range(4):
            if i==0:
                if resps[i]=='V':
                    puntos+=25
                    print('\n' + str(i+1) + '-CORRECTO')
                elif resps[i]=='F':
                    print('\n' + str(i+1) + '-INCORRECTO')
                else:
                    print('\nRESPUESTA ' + str(i+1) + ' INVÁLIDA, PORFAVOR INGRESE LA LETRA V O F\n')
                    puntos=preguntasciencias1(numero_pregunta)
                    break
            else:
                if resps[i]=='F':
                    puntos+=25
                    print(str(i+1) + '-CORRECTO')
                elif resps[i]=='V':
                    print(str(i+1) + '-INCORRECTO')
                else:
                    print('\nRESPUESTA ' + str(i+1) + ' INVÁLIDA, PORFAVOR INGRESE LA LETRA V O F\n')
                    puntos=preguntasciencias1(numero_pregunta)
                    break
        
        return puntos

    elif numero_pregunta==11:
        print('PREGUNTA CIENCIAS 3') #tecnologias
        print('''\tLos aerogeneradores son estructuras con palas que el viento hace girar.
    Estos giros producen energía eléctrica en unos generadores que son movidos por las palas
    del rotor. A igual velocidad del viento, si los aerogeneradores están situados a mayor altitud,
    giran con mayor lentitud. Entre las razones siguientes, ¿cuál es la que mejor explica por qué
    sucede esto? Escriba la letra del inciso de su respuesta.
    
        A) La temperatura es más baja cuando aumenta la altitud.
        B) El aire es menos denso cuando aumenta la altitud.
        C) La gravedad disminuye cuando aumenta la altitud.
        D) Llueve más a menudo cuando aumenta la altitud.''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='B':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasciencias1(numero_pregunta)
        
        return puntos
    
    else:
        return puntos

def preguntasciencias2(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    if numero_pregunta==8:
        print('PREGUNTA CIENCIAS 1') #quimica
        print('''\tEl efecto de la lluvia ácida en el mármol puede simularse sumergiendo astillas
    de mármol en vinagre durante toda una noche. El vinagre y la lluvia ácida tienen
    prácticamente el mismo nivel de acidez. Cuando se pone una astilla de mármol en
    vinagre, se forman burbujas de gas. Puede medirse la masa de la astilla de mármol
    seca antes y después del experimento.
        
    Una astilla de mármol tiene una masa de 2.0 gramos antes de ser sumergida en
    vinagre durante toda una noche. Al día siguiente, la astilla se extrae y se seca.
    ¿Cuál será la masa de la astilla de mármol seca?
    Escriba la letra del inciso de su respuesta.
        
        A) Menos de 2.0 gramos
        B) Exactamente 2.0 gramos
        C) Entre 2.0 y 2.4 gramos
        D) Más de 2.4 gramos''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='A':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasciencias2(numero_pregunta)
        
        return puntos
        
    elif numero_pregunta==10:
        resps=[]
        print('PREGUNTA CIENCIAS 2') #biologia
        print('''\tEn la mayoría de las intervenciones quirúrgicas, los pacientes son anestesiados
    con el fin de evitarles cualquier dolor. ¿Están implicados en la acción de estos gases anestésicos
    los siguientes sistemas del cuerpo humano?
    Responda con SI o NO.\n''')
    
        respuesta1=input('Sistema digestivo: ')
        respuesta1=respuesta1.upper()
        resps = resps + [respuesta1]
        respuesta2=input('Sistema excretor: ')
        respuesta2=respuesta2.upper()
        resps = resps + [respuesta2]
        respuesta3=input('Sistema nervioso: ')
        respuesta3=respuesta3.upper()
        resps = resps + [respuesta3]
        respuesta4=input('Sistema respiratorio: ')
        respuesta4=respuesta4.upper()
        resps = resps + [respuesta4]
        respuesta5=input('Sistema circulatorio: ')
        respuesta5=respuesta5.upper()
        resps = resps + [respuesta5]
        print('\n')
        
        for i in range(5):
            if i==0 or i==1:
                if resps[i]=='NO':
                    puntos+=20
                    print(str(i+1) + '-CORRECTO')
                elif resps[i]=='SI':
                    print(str(i+1) + '-INCORRECTO')
                else:
                    print('\nRESPUESTA ' + str(i+1) + ' INVÁLIDA, PORFAVOR INGRESE LA PALABRA SI O NO\n')
                    puntos=preguntasciencias2(numero_pregunta)
                    break
            else:
                if resps[i]=='SI':
                    puntos+=20
                    print(str(i+1) + '-CORRECTO')
                elif resps[i]=='NO':
                    print(str(i+1) + '-INCORRECTO')
                else:
                    print('\nRESPUESTA ' + str(i+1) + ' INVÁLIDA, PORFAVOR INGRESE LA PALABRA SI O NO\n')
                    puntos=preguntasciencias2(numero_pregunta)
                    break
        
        return puntos

    elif numero_pregunta==12:
        print('PREGUNTA CIENCIAS 3') #fisica
        print('''\tPara beber durante el día, Pedro tiene una taza con café caliente a unos 90ºC de temperatura,
    y una taza con agua mineral fría a unos 5ºC de temperatura. Las tazas son del mismo material y tamaño, y el
    volumen contenido en cada taza es el mismo. Pedro deja las tazas en una habitación donde la temperatura
    es de unos 20ºC. ¿Cuáles serán probablemente las temperaturas del café y del agua mineral después de 10 minutos?
    Escriba la letra del inciso de su respuesta.
        A) 70ºC y 10ºC
        B) 90ºC y 5ºC
        C) 70ºC y 25ºC
        D) 20ºC y 20ºC''')
        
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='A':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntasciencias2(numero_pregunta)
        
        return puntos
    
    else:
        return puntos
#####################################################################################################################################################################
def preguntaslectura1(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    respuestas2=['A','B','C']
    if numero_pregunta==13:
        print('PREGUNTA ESPAÑOL 1')
        print('''\t¿Dónde ____________ una farmacia?
        A) Esta
        B) Está
        C) Es
        D) Hay''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='D':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura1(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==15:
        print('PREGUNTA ESPAÑOL 2')
        print('''\t¿Como se dice?

        A) Detrás mío
        B) Detrás de mí''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='B':
            puntos+=100
            print('\nCORRECTO')
        elif resp=='A':
            print('4-INCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura1(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==17:
        print('PREGUNTA ESPAÑOL 3')
        print('''\tBueno,_________ vienes a comer con nosotros algún día.


    A) a ver si
    B) por qué no
    C) cuando''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='A':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas2:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura1(numero_pregunta)
        
        return puntos
    
    else:
        return puntos
def preguntaslectura2(numero_pregunta):
    puntos=0
    respuestas=['A','B','C','D']
    respuestas2=['A','B','C']
    if numero_pregunta==14:
        print('PREGUNTA ESPAÑOL 1')
        print('''\t Ayer ____________ por ahí de las doce de la noche.

        A) nos hemos acostado
        B) nos acostamos 
        C) nos habiamos acostado
        D) nos acostaríamos ''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='B':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura2(numero_pregunta)
            
        return puntos
    
    elif numero_pregunta==16:
        print('PREGUNTA ESPAÑOL 2')
        print('''\t¿Como se dice?

        A) Encima de él.
        B) Encima de el''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='A':
            puntos+=100
            print('\nCORRECTO')
        elif resp=='B':
            print('4-INCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura2(numero_pregunta)
        
        return puntos
    
    elif numero_pregunta==18:
        print('PREGUNTA ESPAÑOL 3')
        print('''\t¿Cual de las siguientes es la correcta?


    A) Hubo problemas para entrar al concierto
    B) Habían muchos en la pisina
    C) Han habido algunas quejas''')
        resp=input('Respuesta: ')
        resp=resp.upper()
        if resp=='A':
            puntos+=100
            print('\nCORRECTO')
        elif resp in respuestas2:
            print('\nINCORRECTO')
        else:
            print('\nRESPUESTA INVÁLIDA, PORFAVOR INGRESE LA LETRA DE UNO DE LOS INCISOS\n')
            puntos=preguntaslectura2(numero_pregunta)
        
        return puntos
    
    else:
        return puntos

################################################################# I N I C I O   C O D I G O #########################################################################################    
print('Juego de Trivia PISA')
print('¡Bienvenido!\n')
print('Instrucciones del juego:')
print('1. Introduce los nombres de los 2 jugadores.')
print('2. Cada uno de los jugadores va a responder una pregunta previamente asignada.')
print('3. Con cada respuesta correcta, acumularán 100 puntos.\n')
print('¡Suerte!\n')
jugador1=input('Jugador 1: ')
jugador2=input('Jugador 2: ')
print(' ')
puntos1=0
puntos2=0
for i in range(1,19):
    if i%2==0:
        t=2
        print('Turno: ' + str(jugador2))
    else:
        t=1
        print('Turno: ' + str(jugador1))
    if t==1:
        puntos_nuevos=preguntasmate1(i)
        puntos1+=puntos_nuevos
        puntos_nuevos=preguntasciencias1(i)
        puntos1+=puntos_nuevos
        puntos_nuevos=preguntaslectura1(i)
        puntos1+=puntos_nuevos
        print('Puntaje actual: ' + str(puntos1))
    else:
        puntos_nuevos=preguntasmate2(i)
        puntos2+=puntos_nuevos
        puntos_nuevos=preguntasciencias2(i)
        puntos2+=puntos_nuevos
        puntos_nuevos=preguntaslectura2(i)
        puntos2+=puntos_nuevos
        print('Puntaje actual: ' + str(puntos2))
    print('\n\n')
        
print('\nPuntaje final ' + str(jugador1) + ': ' + str(puntos1))
print('Puntaje final ' + str(jugador2) + ': ' + str(puntos2) + '\n')

if puntos1==900:
    print('-------------------------¡Felicidades ' + str(jugador1) + ', obtuviste un puntaje perfecto!-------------------------')
if puntos2==900:
    print('-------------------------¡Felicidades ' + str(jugador2) + ', obtuviste un puntaje perfecto!-------------------------')
if puntos1==0:
    print('-------------------------' + str(jugador1) + ', no te preocupes, ¡Estudia un poco más y vuelve a intentar!-------------------------')
if puntos2==0:
    print('-------------------------' + str(jugador2) + ', no te preocupes, ¡Estudia un poco más y vuelve a intentar!-------------------------')
if puntos1>puntos2:
    print('----------------------------------¡Felicidades ' + str(jugador1) + ', ganaste!----------------------------------')
elif puntos2>puntos1:
    print('----------------------------------¡Felicidades ' + str(jugador2) + ', ganaste!----------------------------------')
else:
    print('-------------------------¡Felicidades ' + str(jugador1) + ' y ' + str(jugador2) + ', han obtenido el mismo puntaje!-------------------------')
    

