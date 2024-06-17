import numpy as np


u = 5              #kapitał początkowy
c = 2              #stała przyrostu          
lambd = 1          #parametr procesu Poissona
eta = 1           #parametr zmiennej losowej wykładniczej

def pol_chin(eta,lambd,c,u):
    return ((eta*lambd)/(c)) * np.exp(-u*((1/eta) - (lambd/c)))

def proc(horizon,u,c,lambd,eta):
    T=0
    while T<=horizon:
        t = np.random.exponential(lambd)
        T += t
        spadek = np.random.exponential(eta)
        u = u + c*t - spadek
        if u <= 0:
            return 0
    return 1

pc = pol_chin(eta,lambd,c,u)

proc1 = np.zeros(10**4)
proc2 = np.zeros(10**4)
proc3 = np.zeros(10**4)
for i in range(10**4):
    proc1[i] = proc(1,u,c,lambd,eta)
    proc2[i] = proc(3,u,c,lambd,eta)
    proc3[i] = proc(20,u,c,lambd,eta)


print(1-sum(proc1)/len(proc1))
print(1-sum(proc2)/len(proc2))
print(1-sum(proc3)/len(proc3))
print(pc)