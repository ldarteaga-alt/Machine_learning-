

# Taller de Regresión Logística

## Objetivo
Explorar computacionalmente propiedades del modelo de regresión logística 
mediante experimentos reproducibles con NumPy, SciPy y Matplotlib.

**Integrantes:** Laura Arteaga y Faber Mongui  
**Universidad El Bosque** — Estadística  
**Semestre:** 2026–2

## Estructura del proyecto

```
Taller_regresion_logistica_26/
├── src/              Código reutilizable
│   ├── modelo.py         Funciones del modelo (sigmoide, RS, etc.)
│   ├── optimizacion.py   Ajuste del modelo con scipy.optimize.minimize
│   └── simulacion.py     Generación de datos simulados
├── notebooks/        Cuaderno de experimentos
│   └── experimentos.ipynb
└── resultados/       Figuras y resultados generados
```

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Idarteaga-alt/Machine_learning-.git
   cd Taller_regresion_logistica_26
   ```

2. Crear un entorno virtual:
   ```bash
   uv venv
   ```

3. Activar el entorno:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

4. Instalar dependencias:
   ```bash
   uv pip install -r requirements.txt
   ```

## Cómo ejecutar

1. Abrir el cuaderno:
   ```
   notebooks/experimentos.ipynb
   ```

2. Seleccionar el kernel correspondiente al entorno virtual.

3. Ejecutar todas las celdas con **Run All**.

Las figuras y resultados se guardarán automáticamente en `resultados/`.
