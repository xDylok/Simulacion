import numpy as np

class modelosMatematicos:
    def __init__(self, p0, r, tiempo):
        self.p0 = p0 # poblacion inicial
        self.r = r # tasa de crecimiento
        self.tiempo = tiempo # tiempo total

    def modeloDeterministico(self):
        t_vector = np.arange(0, self.tiempo + 1)
        poblacion = []
        for i in t_vector:
            p = self.p0 * np.exp(self.r * i)
            poblacion.append(p)
        return t_vector, poblacion

    def modeloDiscreto(self):
        t_vector = np.arange(0, self.tiempo + 1)
        poblacion = []
        poblacion.append(self.p0)
        for i in range(1, self.tiempo + 1):
            poblacionActual = poblacion[-1]
            incremento = (self.r * poblacionActual)
            poblacion.append(poblacionActual + incremento)
        return t_vector, poblacion

    def modeloEstocastico(self, sigma):
        t_vector = np.arange(0, self.tiempo + 1)
        poblacion = []
        poblacion.append(self.p0)
        for i in range(1, self.tiempo + 1):
            poblacionActual = poblacion[-1]
            ruido = np.random.normal(0, sigma)
            nuevaPoblacion = poblacionActual + (self.r * poblacionActual) + ruido
            if nuevaPoblacion < 0:
                nuevaPoblacion = 0
            poblacion.append(nuevaPoblacion)
        return t_vector, poblacion

    def modeloContinuo(self, dt):
        t_vector = np.arange(0, self.tiempo + dt, dt)
        poblacion = []
        poblacion.append(self.p0)
        for i in range(1, len(t_vector)):
            poblacionActual = poblacion[-1]
            cambio = (self.r * poblacionActual)
            poblacion.append(poblacionActual + (dt * cambio))
        return t_vector, poblacion



