import matplotlib.pyplot as plt

class VistaClima:
    def mostrarTabla(self, resultados: list, titulo: str):
        print(f"\n--- {titulo} ---")
        print(f"{'Hora':<6} | {'Humedad':<8} | {'Nubosidad':<10} | {'Temp':<6} | {'H':<4} | {'N':<4} "
              f"| {'Tf':<4} | {'Indice':<6} | Estado")
        print("-" * 80)
        for fila in resultados:
            hora, humedad, nubosidad, temperatura, H, N, Tf, indice, estado = fila
            print(f"{hora:<6} | {humedad:<8} | {nubosidad:<10} | {temperatura:<6} | {H:<4} | {N:<4} | {Tf:<4} | {indice:<6} | {estado}")

    def graficar(self, resultados:list, titulo:str):
        t = [fila[0] for fila in resultados] #tiempo
        P = [fila[7] for fila in resultados] #valores

        plt.figure(figsize=(10, 5))
        plt.plot(t, P, marker='o', label="Indice calculado")

        K = 0.75
        plt.axhline(
            y=K,
            color="red",
            linestyle="--",
            label="Límite para Lluvia (K=0.75)"
        )
        plt.axhline(y=0.40, color='gray', linestyle="--", label='Límite Sin Lluvia (0.40)')

        plt.xlabel("Tiempo (Horas)")
        plt.ylabel("Indice de Lluvia")
        plt.title(titulo)
        plt.grid(True)
        plt.legend()
        # plt.show()

    def mostrarTablas(self):
            plt.show()