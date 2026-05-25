import matplotlib.pyplot as plt
from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns, save_plot
from src.viz import (
    plot_cancellation_distribution,
    plot_cancellations_by_hotel,
    plot_correlation_matrix,
)


def main():
    print("==================================================")
    print("      INICIANDO PIPELINE: HOTEL BOOKINGS 2026     ")
    print("==================================================")

    # 1. Carga de datos usando tu módulo io
    print(f"[1/5] Cargando dataset original desde: {RAW_PATH.name}")
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo en {RAW_PATH}. Revisa 'data/raw/'"
        )
    df = load_csv(RAW_PATH)

    # 2. Limpieza de datos
    print("[2/5] Ejecutando limpieza y tratamiento de anomalías (ADR, Nulos)...")
    df = clean(df)

    # 3. Construcción de características (Feature Engineering)
    print("[3/5] Construyendo las 10 nuevas variables analíticas...")
    df = build_features(df)

    # 4. Validaciones de consistencia con utils
    print("[4/5] Validando integridad del DataFrame procesado...")
    required_cols = ["total_nights", "booking_origin", "season", "total_stay_cost"]
    assert_columns(df, required_cols)

    # 5. Exportación del Dataset Limpio
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(
        f" -> ¡Éxito! Dataset estructurado guardado en: {OUT_PATH.relative_to(OUT_PATH.parents[2])}"
    )

    # 6. EXPORTACIÓN AUTOMÁTICA DE FIGURAS CLAVE
    print("[5/5] Generando y guardando reportes gráficos en 'reports/figures/'...")

    # Forzamos a matplotlib a no bloquear la terminal al generar gráficos en segundo plano
    plt.ioff()

    # Gráfico 1: Distribución de cancelaciones
    plot_cancellation_distribution(df)
    save_plot(plt.gcf(), "cancellation_distribution.png")
    plt.close()

    # Gráfico 2: Cancelaciones cruzadas por tipo de hotel
    plot_cancellations_by_hotel(df)
    save_plot(plt.gcf(), "cancellations_by_hotel.png")
    plt.close()

    # Gráfico 3: Matriz de correlación analítica
    plot_correlation_matrix(df)
    save_plot(plt.gcf(), "correlation_matrix.png")
    plt.close()

    print("==================================================")
    print("   ¡PIPELINE FINALIZADO Y ENTORNO REPRODUCIBLE!   ")
    print("==================================================")


if __name__ == "__main__":
    main()
