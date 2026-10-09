from vista import Vista
from modelo import modelosMatematicos

class Controlador:
    def __init__(self):
        self.datos = [1000, 1100, 1250, 1400, 1600, 1850, 2100]
        self.p0 = self.datos[0]
        self.tiempo = len(self.datos) - 1
        self.r = 0.11
        self.sigma = 40.0
        self.dt = 0.1

        self.K = 2500

        self.modelo = modelosMatematicos(self.p0, self.r, self.tiempo)
        self.vista = Vista()

    def ejecutar(self):
        t_det, p_det = self.modelo.modeloDeterministico()
        t_disc, p_disc = self.modelo.modeloDiscreto()
        t_est, p_est = self.modelo.modeloEstocastico(self.sigma)
        t_cont, p_cont = self.modelo.modeloContinuo(self.dt)
        self.vista.graficar(t_det, p_det, t_disc, p_disc, t_est, p_est, t_cont, p_cont, self.datos, self.K)
if __name__ == '__main__':
    app = Controlador()
    app.ejecutar()