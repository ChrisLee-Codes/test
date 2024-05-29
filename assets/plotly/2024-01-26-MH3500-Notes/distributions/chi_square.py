import plotly.graph_objects as go
import numpy as np
import math


def gamma_distribution(x, alpha, beta):
    if x <= 0:
        return 0
    else:
        return (x ** (alpha - 1) * np.exp(-x / beta)) / (
            beta**alpha * math.gamma(alpha)
        )


def chi_square_distribution(x, n):
    return gamma_distribution(x, n / 2, 2)


fig = go.Figure(layout_yaxis_range=[0, 1])

Ns = np.arange(1, 10, 1)

for step in Ns:
    x = np.arange(0, 15, 0.01)
    y = [gamma_distribution(i, step, 1) for i in x]
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
    title="Chi-Square Distribution (n = 2)",
)

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": f"n = {Ns[i]}"},
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
                    {"visible": [n == step for step in Ns]},
                    {"title": f"Chi-Square Distribution (n = {n})"},
                ],
            )
            for n in Ns
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("chi_square.html", auto_open=True)

fig = go.Figure()
