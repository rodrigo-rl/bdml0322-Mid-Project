def tabla_partidos(partidos):
    
    llaves=list(partidos)[1:]
    valores=list(partidos.values())[1:]

    stage=[]
    dia=[]
    team=[]
    rival=[]
    result=[]

    for i in range(1,len(valores),6):

        #partido de la fase - se quita el nº de partido en la fase de grupos 
        if re.search('^Gr.*',llaves[i]):
            stage.append('Group stage')
        else:     
            stage.append(llaves[i])
    
        #fecha del partido
        dia.append(valores[i])
    
        #Equipos y resultados (si hay pensaltis entre paréntesis)
        if valores[i+2]!=0:
            team.append(f"{valores[0]} - {valores[i+1]} ({valores[i+2]})")
            rival.append(f"{valores[i+4]} ({valores[i+5]}) - {valores[i+3]}")
        else:
            team.append(f"{valores[0]} - {valores[i+1]}")
            rival.append(f"{valores[i+4]} - {valores[i+3]}")

        #resultado del partido
        if valores[i+1]>valores[i+4]:
            result.append('Victory')
        elif valores[i+1]<valores[i+4]:
            result.append('Defeat')
        elif valores[i+1]==valores[i+4]:
            if valores[i+2]>valores[i+5]:
                result.append('Victory')
            else:
                result.append('Defeat')

    d_partidos={'Stage':stage,'Date':dia, 'Team':team, 'Rival':rival, 'Result':result}    
    return d_partidos
    
def tabla_jugadores(jugadores):
    jugador=[]
    num=[]
    
    jug_gol={}
    jug_yel={}
    jug_red={}


    nom_jug=list(jugadores.keys())
    atrib_jug=list(jugadores.values())

    for i in range(2,len(nom_jug)):

        #Obtenemos el nombre y el número del jugador
        jugador.append(nom_jug[i])
        num.append(str(atrib_jug[i][0]))
        
        tantos=[]
        amar=[]
        roja=[]

        #Obtenemos los goles y las tarjetas que les han sacado 
        for j in range(1,len(atrib_jug[i])):
    
            if re.search('Go.*',atrib_jug[i][j]):
                tantos.append(atrib_jug[i][j])
            elif re.search('Ye.*',atrib_jug[i][j]):
                amar.append(atrib_jug[i][j])
            elif re.search('Re.*',atrib_jug[i][j]):
                roja.append(atrib_jug[i][j])
        jug_gol[nom_jug[i]]=tantos
        jug_yel[nom_jug[i]]=amar
        jug_red[nom_jug[i]]=roja

        
    d_jugadores={'Name':jugador,'Num':num, 'Tantos':jug_gol, 'Amarillas':jug_yel, "Rojas":jug_red}    
    return d_jugadores
    

from operator import attrgetter
import streamlit as st
import streamlit.components.v1 as components
import re
import pandas as pd
from data.get_data import players, teams, goals
 
st.title('EURO-CUP 2020.py')
st.text('En este dashboard se van a mostrar algunos datos sobre las selecciones') 
st.text('que participaron en la competición') 

goles=list(goals()[0])[1:]

team_choosed=st.multiselect('Elige el equipo para mostrar los resultados de los partidos', sorted(goles))


if len(team_choosed)==1:
    partidos=teams(team_choosed[0])[0] #se elige el equipo
    jugadores=players(team_choosed[0])[0]

    d_partidos_first =tabla_partidos(partidos) #se obtiene una tabla con los resultados del partido

    dataf_partidos_first=pd.DataFrame(data=d_partidos_first) #se convierte en un df

    st.table(dataf_partidos_first.iloc[0:len(dataf_partidos_first.index)]) #visualización

    stats=st.button('Click me to show the players stats') #botón para ver más información de los jugadores 

    d_jugadores_first =tabla_jugadores(jugadores) #subrutina de la que se obtiene una tabla

    goal=[] #vienen los goles y tarjetas por cada partido y cada jugador, se cuentan cuantos han metido en la competición
    for i in d_jugadores_first["Tantos"].values():
        goal.append(len(i))
    yellow=[]
    for i in d_jugadores_first["Amarillas"].values():
        yellow.append(len(i))
    red=[]
    for i in d_jugadores_first["Rojas"].values():
        red.append(len(i))


    if stats==True: #en el caso de que se pulse o no el botón cambia la información
        d_jugador={'Name':d_jugadores_first['Name'],'Num':d_jugadores_first["Num"], 'Goals':goal, 'Yellow Cards':yellow, 'Red Cards':red}
        dataf_jugador =pd.DataFrame(data=d_jugador)
    else:
        d_jugador={'Name':d_jugadores_first["Name"],'Num':d_jugadores_first["Num"]}
        dataf_jugador =pd.DataFrame(data=d_jugador)


    st.table(dataf_jugador.iloc[0:len(d_jugadores_first["Name"])]) #se visualiza la información de los jugadores


elif len(team_choosed)==2: #en el caso que se busque ver un partido en concreto se eligen los dos equipos
    
    partidos_first=teams(team_choosed[0])[0] #equipo y jugadores 
    jugadores_first=players(team_choosed[0])[0]

    partidos_second=teams(team_choosed[1])[0] #equipo y jugadores 
    jugadores_second=players(team_choosed[1])[0]

    d_partidos_first =tabla_partidos(partidos_first) #hay que repetir los resultados porque no se pueden obtener de la otra parte del if   
    d_jugadores_first =tabla_jugadores(jugadores_first)
    dataf_partidos_first=pd.DataFrame(data=d_partidos_first)


    coincidencia=False #se ve si se ha celebrado el partido o se ha elegido una combinación que no ha ocurrido
    for fila in range(len(dataf_partidos_first['Rival'])):
        if dataf_partidos_first['Rival'][fila].split(" ")[-1]==team_choosed[1]:
            coincidencia=True
            break
    
    if coincidencia==False: #si no hay partido se avisa de que no hay datos
        st.header("Please, choose another teams combination.")
        st.header("These two teams didn't play together.")
    elif coincidencia==True: #en el caso de que sí que se jugara:

        col1, col2,col3 = st.columns(3) #tabla de columnas con información del partido
        col1.write(team_choosed[0]) #columna izquierda - equipo 1
        col2.write(dataf_partidos_first['Stage'][fila]) #información general
        col3.write(team_choosed[1])#columna derecha - equipo 2

        d_jugadores_second =tabla_jugadores(jugadores_second)
        
        goal_first=[]
        goal_second=[]

        for i,j in d_jugadores_first['Tantos'].items(): #se saca la info de los goles de cada jugador
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       goal_first.append(i)
        
        col1.write(f"{len(goal_first)}")
        col1.write("----GOALS----")

        for i in goal_first:
            col1.write(f"{i}")
        col1.write("----Yellow Cards----")

        for i,j in d_jugadores_second['Tantos'].items():
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       goal_second.append(i)
        
        col3.write(f"{len(goal_second)}")
        col3.write("----GOALS----")
        
        for i in goal_second:
            col3.write(f"{i}")
        col3.write("----Yellow Cards----")

        if dataf_partidos_first['Result'][fila]=='Victory': #quien gana y pierde
            if len(goal_first)==len(goal_second):
                col2.write(f"Victory of {team_choosed[0]} in pens")
            else:
                col2.write(f"Victory of {team_choosed[0]}")
        elif dataf_partidos_first['Result'][fila]=='Defeat':
            if len(goal_first)==len(goal_second):
                col2.write(f"Victory of {team_choosed[1]} in pens")
            else:
                col2.write(f"Victory of {team_choosed[1]}")



        yellow_first=[]
        yellow_second=[]
        red_first=[]

        for i,j in d_jugadores_first['Amarillas'].items():
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       yellow_first.append(i)
                
        for i in yellow_first:
            col1.write(f"{i}")
        col1.write("----Red Cards----")
        
        for i,j in d_jugadores_second['Amarillas'].items():
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       yellow_second.append(i)
                
        for i in yellow_second:
            col3.write(f"{i}")
        col3.write("----Red Cards----")      
        
        red_first=[]
        red_second=[]

        for i,j in d_jugadores_first['Rojas'].items():
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       red_first.append(i)
                
        for i in red_first:
            col1.write(f"{i}")
        col1.write("--------")
        
        for i,j in d_jugadores_second['Rojas'].items():
            if j!=[]:
                for g in j:
                    if " ".join(g.split(" ")[1:])==dataf_partidos_first['Stage'][fila]:
                       red_second.append(i)
                
        for i in red_second:
            col3.write(f"{i}: Yellow card")
        col3.write("--------")      
