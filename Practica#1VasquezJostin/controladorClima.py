from vistaClima import VistaClima

class ControladorClima:
    def __init__(self, modeloClima, vistaClima):
        self.modeloClima = modeloClima
        self.vistaClima = vistaClima

    def ejecutarSimulacion(self, datos:list):
        # Simular el modelo originial
        resultadosOriginal = self.modeloClima.procesarSimulacion(datos, ModeloAjustado=False)
        self.vistaClima.mostrarTabla(resultadosOriginal, "Tabla Modelo Orignal")
        self.vistaClima.graficar(resultadosOriginal, "Comportamiento Modelo Orignal")
        #simular modelo ajustado
        resultadosAjustados = self.modeloClima.procesarSimulacion(datos, ModeloAjustado=True)
        self.vistaClima.mostrarTabla(resultadosAjustados, "Tabla Modelo Ajsutado")
        self.vistaClima.graficar(resultadosAjustados, "Comportamiento Modelo Ajsutado")
