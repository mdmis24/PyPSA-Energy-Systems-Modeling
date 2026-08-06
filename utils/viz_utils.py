import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def set_nature_style():
    """Applies publication-quality 'Nature' styling to matplotlib globally.

    This only sets rcParams (fonts, spines, grid, figure size, dpi, etc.).
    It never sets a color — color is chosen per-call in plot_timeseries().
    """
    mpl.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 11,
        'axes.linewidth': 0.8,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'lines.linewidth': 1.5,
        'figure.figsize': (7, 3.5),  # 2:1 aspect ratio fits publication columns better
        'figure.dpi': 300,
        'grid.color': '#e0e0e0',
        'grid.linewidth': 0.5,
        'axes.grid': True,
        'axes.facecolor': 'white',
        'figure.facecolor': 'white',
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.major.size': 3,
        'ytick.major.size': 3,
    })


# Call style once when the module is imported, so any notebook that does
# `from viz_utils import plot_timeseries` gets the house style automatically.
set_nature_style()


def plot_timeseries(
    data,
    column=None,
    title='Time Series',
    xlabel='Time',
    ylabel='Value',
    color='#1f77b4',
    figsize=None,
    **kwargs,
):
    """Plot a time series using the shared 'Nature' style.

    viz_utils only controls the *style* (fonts, spines, grid, figure size).
    The *color* of a given plot is always whatever you pass in `color=` here
    — it is never hardcoded inside this module, so different notebooks/cells
    can use different colors without touching viz_utils.

    Parameters
    ----------
    data : pd.DataFrame or pd.Series
    column : str, optional
        Column to plot if `data` is a DataFrame. If omitted, the first
        column is used.
    color : str
        Line color for this specific plot (e.g. 'black', '#f39c12').
    """
    if isinstance(data, pd.DataFrame):
        if column is not None:
            series = data[column]
        else:
            series = data.iloc[:, 0]
    elif isinstance(data, pd.Series):
        series = data
    else:
        raise TypeError('Expected a pandas DataFrame or Series')

    # Dense series (e.g. 8760 hourly points) look like a solid smeared block
    # at the default lines.linewidth=1.5, fully opaque. Thin + slightly
    # transparent keeps full-year hourly plots readable. Only applied when
    # the caller hasn't already specified linewidth/alpha themselves.
    plot_kwargs = dict(kwargs)
    if len(series) > 2000:
        plot_kwargs.setdefault('linewidth', 0.5)
        plot_kwargs.setdefault('alpha', 0.85)

    fig, ax = plt.subplots(figsize=figsize)
    series.plot(ax=ax, color=color, **plot_kwargs)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    fig.tight_layout()
    plt.show()
    return fig, ax


# Alias for backward compatibility
plot_price_data = plot_timeseries
