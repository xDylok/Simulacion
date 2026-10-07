# Práctica #1: Simulación del Clima

**Autor:** Jostin Xavier Vasquez Calderón  
**Institución:** Universidad Nacional de Loja - Carrera de Computación  

## Descripción del Proyecto
Este proyecto es un modelo de simulación climática desarrollado en Python. Calcula la probabilidad de lluvia basándose en variables meteorológicas (humedad, nubosidad y temperatura) aplicando un índice matemático. Además, implementa un factor de ajuste ($K=0.75$) para comparar el comportamiento del clima bajo diferentes condiciones.

El proyecto está estructurado utilizando el patrón de diseño **MVC (Modelo-Vista-Controlador)** para separar la lógica de cálculo, la presentación de datos y el flujo de ejecución.

## Estructura del Proyecto
* `main.py`: Punto de entrada de la aplicación.
* `modeloClima.py`: Contiene la lógica matemática, el cálculo de índices y la determinación de estados (Lluvia, Baja posibilidad, Sin lluvia).
* `vistaClima.py`: Se encarga de renderizar las tablas en la consola y generar las gráficas de comportamiento.
* `controladorClima.py`: Orquesta la comunicación entre el modelo y la vista.
* `requirements.txt`: Archivo de dependencias generadas vía `pip freeze`.

## Requisitos Previos
* Python 3.12 o superior.
* Instalador de paquetes `pip` (incluido por defecto con Python).

## Instalación y Ejecución

1. Clonar el repositorio:
   ```
   git clone "https://github.com/xDylok/Simulacion.git"
   cd Practica#1VasquezJostin

2. Crear el entorno virtual
   ```
   python3 -m venv .venv

3. Activar el entorno virtual
   
   - Linux/MacOS:
   ``` 
   source .venv/bin/activate 
   ```
   - Windows:
   ```
   .venv/Scripts/activate
   ```
4. Instalar los requerimientos
   ```
   pip install -r requirements.txt
   ```
5. Ejecutar la simulacion
   ```
   python main.py
   ```