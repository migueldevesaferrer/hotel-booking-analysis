# Hotel Booking Analysis Project

Este proyecto proporciona una plantilla reproducible y modularizada para llevar a cabo un Análisis Exploratorio de Datos (EDA) completo, limpieza exhaustiva y construcción de variables (*Feature Engineering*) sobre un conjunto de datos de reservas hoteleras.

### 1) Objetivo
El objetivo principal es identificar los patrones de comportamiento de los huéspedes en hoteles urbanos y de tipo resort, aislando los factores que mayor impacto tienen sobre las cancelaciones de reservas y la variabilidad de precios (ADR).

### 2) Dataset
- **Fuente:** `data/raw/hotel_booking.csv`
- **Características:** Contiene registros de reservas individuales que detallan la fecha de llegada, la composición del grupo familiar, el régimen de comidas, el precio medio diario (ADR) y el estado final de la reserva (`is_canceled`).

### 3) Preguntas de Investigación
- **Q1:** ¿Qué canales de distribución y segmentos de mercado representan el mayor riesgo de cancelación para el negocio?
- **Q2:** ¿Cómo afecta la anticipación de la reserva (*lead time*) a la tasa de cancelación final?
- **Q3:** ¿Existe un comportamiento estacional claro en las tarifas hoteleras y el volumen de ocupación?

### 4) Data Issues & Fixes
- **Columnas Sintéticas e Irrelevantes:** Se eliminaron datos sensibles de simulación (`name`, `email`, `phone-number`, `credit_card`) que añadían ruido al análisis.
- **Valores Nulos:** Imputación controlada según el contexto de negocio:
  - `children`, `company`, `agent` rellenados con `0` (indicando ausencia de niños, empresa o agente mediador).
  - `country` rellenado con la categoría `"Unknown"`.
- **Anomalías en Tarifas (ADR):** Se eliminaron registros con valores negativos de facturación y se aplicó un truncamiento (*clip*) en un umbral máximo de 600 para controlar *outliers* extremos de suites de lujo.

### 5) Pipeline de Ejecución
El proyecto se ejecuta de forma secuencial mediante una arquitectura modular:
`data/raw/` (Datos brutos) → `src/cleaning.py` (Limpieza) → `src/features.py` (Nuevas Variables) → `data/processed/` (Salida reproducible).

### 6) Hallazgos e Insights Clave
1. **Volatilidad Urbana:** Los hoteles de ciudad (*City Hotels*) concentran una tasa de cancelación significativamente superior a los complejos vacacionales (*Resort Hotels*), influenciados por segmentos altamente modificables como *TA/TO* o *Groups*.
2. **Riesgo por Anticipación:** Se validó estadísticamente que a mayor *lead time* (especialmente en reservas categorizadas como "Very Long"), el ratio de cancelaciones se dispara, sugiriendo políticas estrictas de depósitos no reembolsables.
3. **Pico Estacional:** El verano (*Summer*) representa la temporada con mayor volumen absoluto de reservas e ingresos, donde el ADR experimenta distribuciones más amplias y tarifas más competitivas.

---

### 7) Estructura del Proyecto
```text
project/
├── main.py                 # Ejecuta la carga, limpieza, ingeniería y guarda reportes
├── requirements.txt
├── .gitignore
├── README.md               # Explicación del proyecto, insights y preguntas
├── data/
│   ├── raw/
│   │   └── hotel_booking.csv  # Archivo original (entrada)
│   └── processed/
│       └── hotel_booking_clean_features.csv  # Creado por main.py (salida de datos)
├── notebooks/
│   └── eda.ipynb           # Importa tus funciones de src/ para hacer la narrativa
├── reports/
│   └── figures/            # Creado automáticamente por main.py (salida visual)
│       ├── cancellation_distribution.png
│       ├── cancellations_by_hotel.png
│       └── correlation_matrix.png
└── src/
    ├── __init__.py         # Archivo vacío para que Python reconozca el módulo
    ├── config.py           # Centralización de rutas absolutas basadas en ROOT
    ├── io.py               # Lógica de lectura (load_csv)
    ├── cleaning.py         # Filtros y corrección de nulos/outliers
    ├── features.py         # Creación de las 10 columnas y tipos de datos
    ├── viz.py              # Tus 22 visualizaciones empaquetadas en funciones limpias
    └── utils.py            # Guardado de imágenes y aserciones de control
