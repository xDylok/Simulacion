from vistaClima import VistaClima

class ControladorClima:
    def __init__(self, modeloClima, vistaClima):
        self.modeloClima = modeloClima
        self.vistaClima = vistaClima

    def ejecutarSimulacion(self, datos:list):
        # Simular el modelo originial
        resultadosOriginal = self.modeloClima.procesarSimulacion(datos, ModeloAjustado=False)
        self.vistaClima.mostrarTabla(resultadosOriginal, "Tabla Modelo Orignal")
        self.vistaClima.graficar(resultadosOriginal, "Comportamiento Modelo Orignal: I= 0.5H + 0.3N + 0.2Tr")

        #simular modelo ajustado
        resultadosAjustados = self.modeloClima.procesarSimulacion(datos, ModeloAjustado=True)
        self.vistaClima.mostrarTabla(resultadosAjustados, "Tabla Modelo Ajsutado")
        self.vistaClima.graficar(resultadosAjustados, "Comportamiento Modelo Ajsutado: I= 0.2H + 0.7N + 0.1Tr")

        self.vistaClima.mostrarTablas()
