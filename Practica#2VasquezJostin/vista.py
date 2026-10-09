import matplotlib.pyplot as plt

class Vista:
    def graficar(self, t_det, p_det, t_disc, p_disc, t_est, p_est, t_cont, p_cont, datos_reales, K):
        plt.figure(figsize=(10, 5))

        plt.plot(t_det, p_det, label="Determinístico", linestyle='-')
        plt.plot(t_disc, p_disc, label="Discreto", linestyle='--')
        plt.plot(t_est, p_est, label="Estocástico", marker='.')
        plt.plot(t_cont, p_cont, label="Continuo", linestyle='-.')

        t_reales = range(len(datos_reales))
        plt.plot(t_reales, datos_reales, label="Datos Originales", marker='o', color='black')

        plt.axhline(
            y=K,
            linestyle="--",
            label="Capacidad máxima K",
            color="red"
        )

        plt.xlabel("Tiempo")
        plt.ylabel("Población")
        plt.title("Comparación de modelos de crecimiento poblacional")
        plt.grid(True)
        plt.legend()

        plt.show()