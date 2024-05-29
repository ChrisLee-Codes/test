import plotly.graph_objects as go
import numpy as np
import math


def t_distribution(x, n):
    return (
        math.gamma((n + 1) / 2)
        / (math.sqrt(n * math.pi) * math.gamma(n / 2))
        * math.pow(1 + math.pow(x, 2) / n, -(n + 1) / 2)
    )


def distribution(x, n):
    return t_distribution(x, n)


def get_title(n):
    title = f"t<sub>{n}</sub>-Distribution"
    if n == "∞":
        title += " (Standard Normal Distribution)"
    return title


def normal_distribution(x):
    return math.exp(-(x**2) / 2) / math.sqrt(2 * math.pi)


fig = go.Figure()

Ns = [1, 2, 3, 4, 5, 10, 30, 50, 100]

for step in Ns:
    x = np.arange(-5, 5, 0.001)
    y = [distribution(i, step) for i in x]
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            name="n = " + str(step),
            x=x,
            y=y,
        )
    )

fig.data[1].visible = True
fig.update_layout(
    title=get_title(2),
)

x = np.arange(-5, 5, 0.005)
y = [normal_distribution(i) for i in x]
fig.add_trace(
    go.Scatter(
        visible=True,
        # line=dict(color="#00CED1", width=6),
        name="Normal Distribution",
        x=x,
        y=y,
    )
)

# Create and add slider
steps = []
for i in range(len(Ns)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": get_title(Ns[i])},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)


sliders = [
    dict(
        active=1,
        steps=[
            dict(
                label=f"n = {n}",
                method="update",
                args=[
                    {"visible": [n == step for step in Ns] + [True]},
                    {"title": get_title(n)},
                ],
            )
            for n in Ns
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("t_distribution.html", auto_open=True)

fig = go.Figure()
