import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# =====================================================================
# 1. ANÁLISIS UNIVARIADO
# =====================================================================


def plot_cancellation_distribution(df: pd.DataFrame):
    """Grafica la distribución de la variable objetivo (Cancelaciones)."""
    plt.figure(figsize=(10, 3))
    sns.countplot(data=df, y="is_canceled", palette=["#4CAF50", "#F44336"])
    plt.title("Booking Cancellation Distribution")
    plt.ylabel("Canceled (0 = No, 1 = Yes)")
    plt.xlabel("Count")
    plt.tight_layout()
    plt.show()


def plot_numerical_distribution(
    df: pd.DataFrame, col: str, bins: int = 50, plot_type: str = "hist"
):
    """
    Grafica la distribución de variables numéricas (Lead time, ADR, etc.).
    Soporta histogramas ('hist') y diagramas de violín ('violin').
    """
    plt.figure(figsize=(10, 3))
    if plot_type == "hist":
        sns.histplot(df[col], bins=bins, kde=True)
        plt.title(f"{col.replace('_', ' ').title()} Distribution")
    elif plot_type == "violin":
        sns.violinplot(x=df[col])
        plt.title(f"{col.upper()} Distribution")

    plt.tight_layout()
    plt.show()


def plot_categorical(df: pd.DataFrame, col: str):
    """
    Genera un gráfico de barras con la distribución porcentual de una variable categórica.
    Sirve para automatizar las 13 variables categóricas de tu bucle en el notebook.
    """
    plt.figure(figsize=(10, 3))
    data = df[col].value_counts(normalize=True).mul(100).sort_values(ascending=False)
    sns.barplot(x=data.index, y=data.values)
    plt.title(f"Distribution of {col}")
    plt.ylabel("Percentage (%)")
    plt.xlabel(col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# =====================================================================
# 2. ANÁLISIS BIVARIADO
# =====================================================================


def plot_cancellations_by_hotel(df: pd.DataFrame):
    """Compara el volumen de cancelaciones según el tipo de hotel."""
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="hotel", hue="is_canceled", palette=["#4CAF50", "#F44336"])
    plt.title("Cancellations by Hotel Type")
    plt.xlabel("Hotel Type")
    plt.ylabel("Count")
    plt.legend(["Not Canceled", "Canceled"])
    plt.tight_layout()
    plt.show()


def plot_adr_by_hotel(df: pd.DataFrame):
    """Muestra la distribución del ADR por tipo de hotel mediante diagramas de violín."""
    plt.figure(figsize=(10, 5))
    sns.violinplot(
        data=df,
        x="hotel",
        y="adr",
        cut=0,
        inner="quartile",
    )
    plt.title("ADR Distribution by Hotel Type")
    plt.tight_layout()
    plt.show()


def plot_cancellation_rate_by_market(df: pd.DataFrame):
    """Muestra la tasa media de cancelación por cada segmento de mercado."""
    plt.figure(figsize=(8, 4))
    cancel_rate = (
        df.groupby("market_segment")["is_canceled"].mean().sort_values(ascending=False)
    )
    cancel_rate.plot(kind="bar")
    plt.title("Cancellation Rate by Market Segment")
    plt.ylabel("Cancellation Rate")
    plt.tight_layout()
    plt.show()


def plot_bookings_by_season_and_hotel(df: pd.DataFrame):
    """Muestra el volumen de reservas cruzando temporada y tipo de hotel."""
    plt.figure(figsize=(10, 5))
    sns.countplot(
        data=df,
        x="season",
        hue="hotel",
    )
    plt.title("Bookings by Season and Hotel Type")
    plt.xlabel("Season")
    plt.ylabel("Number of Bookings")
    plt.legend(title="Hotel Type")
    plt.tight_layout()
    plt.show()


def plot_booking_origin_by_hotel(df: pd.DataFrame):
    """Muestra el origen de la reserva por tipo de hotel."""
    plt.figure(figsize=(10, 5))
    sns.countplot(
        data=df,
        x="booking_origin",
        hue="hotel",
        order=df["booking_origin"].value_counts().index,
    )
    plt.title("Booking Origin by Hotel Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# =====================================================================
# 3. MATRIZ DE CORRELACIÓN
# =====================================================================


def plot_correlation_matrix(df: pd.DataFrame):
    """Filtra las variables numéricas y genera su mapa de calor de correlación."""
    plt.figure(figsize=(12, 8))
    corr = df.select_dtypes(include=np.number).corr()
    sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=False,  # Cambiar a True si quieres ver los números exactos
        fmt=".2f",
    )
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
