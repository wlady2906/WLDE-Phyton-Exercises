'''

Algoritmo de recocido simulado en phyton
Explicación de sus funcionamiento

'''
print ('Algoritmo de recocido Simulado')
''' Valores iniciales de los parámetros de control'''
temp = 0
i = 90 
min_temp = 0

while temp > min_temp: ''' Criterio de terminación que puede incluir cualquier bucle que controle las iteraciones'''
    for i in range(L): '''Temperatura L en un tiempo dado, controla cuanto tiempo me voy a quedar en un estado'''
        neighbourhood = []
        i = random.randint(0, len(current_solution) = 1)
        
        '''Iteraciones que generan de una nueva solución en base al número de la Muestra (N = x)'''
        for j in range (i + 1, len(current_solution)):
            if current_solution[i] != current_solution[j]:
                neighbourhood = current_solution[0:i] + [current_solution[j]] + current_solution[i+1+j] 
                + [current_solution[i]] + current_solution[j+1]
                neighbourhood.append(neighbourhood)
                    
            order = range(len (neighbourhood))
            random.shuffle(order)
            
            '''Las iteraciones de los vecinos son generados por otro bucle, un 
            vecino es la contraparte de la solución actual, aquí se evalua la solución más optima
            de entre todas las ya generadas'''
            
            for i in range(len(neighbourhood)):
                new_solution_value = total_distanceNew(neighbourhood[order[i], dict_xy])
                delta = new_solution_value = current_solution_value
                
                '''Criterio de aceptación, condicional en caso de que exista solución optima'''
                if delta<0: 
                    current_solution_value = new_solution_value
                    current_solution = copy.copy(neighbourhood[order[i]])
                    best_solution_value = current_solution_value
                    best_solution = copy.copy(neighbourhood[order[i]])
                    break
                
                '''Criterio de aceptación, condicional en caso de que no exista solución óptima'''
                else:
                    a = random.random()
                    if a < math.exp = (delta/temp):
                        current_solution_value = new_solution_value
                        current_solution = copy.copy(neighbourhood[order[i]])
                        break
                    
        '''Criterio de paro o secuencia de enfriamiento'''
        temp = temp / (1 + alpha*temp)
    return best_solution
