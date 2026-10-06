# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from modeloClima import ModeloClima
from vistaClima import VistaClima
from controladorClima import ControladorClima

if __name__ == "__main__":
    # Hora, Humedad, Nubosidad, Temperatura
    datos_clima = [
        ("06:00", 65, 40, 14),
        ("08:00", 70, 50, 16),
        ("10:00", 68, 45, 18),
        ("12:00", 60, 30, 22),
        ("14:00", 75, 70, 20),
        ("16:00", 85, 85, 18),
        ("18:00", 92, 95, 16),
        ("20:00", 88, 90, 17),
        ("22:00", 80, 75, 15)
    ]

    # inicializacion MVC
    ModeloClima = ModeloClima()
    VistaClima = VistaClima()
    ControladorClima = ControladorClima(ModeloClima, VistaClima)

    # Ejec
    ControladorClima.ejecutarSimulacion(datos_clima)