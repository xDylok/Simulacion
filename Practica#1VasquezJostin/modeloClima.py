
class ModeloClima:
    def obtenerTf(self, temperatura:float) -> float:
        # asignacion del factor de temp segun la tabla de TF
        if temperatura <= 10: return 1.00
        elif temperatura >= 28: return 0.10
        else: return round(1-((temperatura-10)*0.05), 2) #round redondea el numero a 2 cifras,

    def calcularIndice(self, Humedad: float, Nubosidad: float, FactorTemp: float,
                       ModeloAjustado: bool = False) -> float:
        if ModeloAjustado:
            # ajuste de modelo
            indice = 0.2 * Humedad + 0.7 * Nubosidad + 0.1 * FactorTemp
            return round(indice, 2)
        else:
            # modelo original
            indice = 0.5 * Humedad + 0.3 * Nubosidad + 0.2 * FactorTemp
            return round(indice, 2)

    def determinarEstado(self, indice: float) ->str:
        # clasificacion de indices segun tabla de reglas
        if indice < 0.40:
            return "Sin lluvia"
        elif 0.40 <= indice < 0.60:
            return "Baja posibilidad"
        elif 0.60 <= indice < 0.75:
            return "Lluvia probable"
        elif indice >= 0.75:
            return "Lluvia"

    def procesarSimulacion(self, datos:list, ModeloAjustado:bool = False) -> list:
        resultados = []
        for hora, humedad, nubosidad, temperatura in datos:
            H = humedad/100.00
            N = nubosidad/100.00
            Tf = self.obtenerTf(temperatura)

            indice = self.calcularIndice(H, N, Tf, ModeloAjustado)
            estado = self.determinarEstado(indice)

            resultados.append((hora, humedad, nubosidad, temperatura, H, N, Tf, round(indice, 2), estado))
        return resultados
