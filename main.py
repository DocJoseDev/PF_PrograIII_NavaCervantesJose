import modelo


# CREAR EL ENTORNO VIRTUAL (si o si esta version)
# python -3.11 -m venv .venv

# Habilitar el entorno virtual (en Windows)
# source .venv/bin/activate

# Instalar las dependencias

def prediccion(modelo):
    resultado = modelo.predict(100)
    print(f'La temperatura {100.0}°C es igual a {resultado}°F')


if __name__ == "__main__":
    modelo, historial = modelo.entrenar_modelo()
    #graficas.graficas(historial)
    prediccion(modelo)

