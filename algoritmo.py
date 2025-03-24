import numpy as np 
import math
# Metodo de Newton

#Nº de barras, tipo de barra, 1 angulo teta, 2 de admitância, Matriz de admitancia, resistencias e impedancias shunt associados, derivadas parciais

def main():

    n_barras = 2
    t_barra = ["pq", "vt"]
    n_barrasPV = 2
    n_barrasPQ = 2
    
    ang_teta = 0
    gx = [10, 5]
    p2_esp = 350
    q2_esp = 2
    err_ = 0.001


    matriz_admi = np.array([[40+2j, 30], [19, 87-5j]])
    G_ = np.real(matriz_admi)
    B_ =np.imag(matriz_admi)

    
    # while True:
    pcalc= 1*(2*(np.sum(G_)* math.cos(0)+(np.sum(B_))* math.sin(0)))
    qcalc= 2*(1*(np.sum(G_)* math.sin(0)+(np.sum(B_))* math.cos(0)))

    D_p2 = p2_esp - pcalc
    D_q2 = q2_esp - qcalc

    print (D_p2) 
    print (D_q2) 

    if D_p2 > err_ or D_q2 > err_:
        p2_esp = D_p2
        q2_esp = D_q2

        # else:
            # break

    matriz_H = np.array([[40+2j, 30], [19, 87-5j]])
    

if __name__ == "__main__":
    main()