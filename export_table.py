import pandas as pd
import matplotlib.pyplot as plt


def export_table_png(data, name):
    df = pd.DataFrame(data)
    cell_width = max(df.astype(str).apply(lambda col: col.map(len)).max()) * 0.3
    fig_width = cell_width * len(df.columns)
    fig_height = 0.6 + 0.4 * len(df)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.axis('off')
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    plt.tight_layout()
    plt.savefig(name, dpi=400)
