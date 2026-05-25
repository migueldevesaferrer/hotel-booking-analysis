import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_total_by_category(df, category_col="product_line", value_col="total"):
    order = df.groupby(category_col)[value_col].sum().sort_values().index
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x=category_col, y=value_col, estimator=np.sum, order=order)
    plt.title(f"Total {value_col} by {category_col}")
    plt.tight_layout()
    plt.show()
