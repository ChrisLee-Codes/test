import plotly.graph_objects as go
import numpy as np
import math


def F_distribution(w, m, n):
    if w <= 0:
        return 0
    return (
        math.gamma((m + n) / 2)
        / (math.gamma(m / 2) * math.gamma(n / 2))
        * math.pow(m / n, m / 2)
        * math.pow(w, m / 2 - 1)
        * math.pow(1 + m / n * w, -(m + n) / 2)
    )


fig = go.Figure(layout_yaxis_range=[0, 1])

Ms = [1, 2, 3, 4, 5, 10, 20, 50, 100]

for step in Ms:
    x = np.arange(0, 10, 0.001)
    y = [F_distribution(i, step, 10) for i in x]
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            name=f"m = {step}",
            x=x,
            y=y,
        )
    )

# Make 10th trace visible
fig.data[3].visible = True
fig.update_layout(
    title="F(4, 10) Distribution",
)

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": f"F({Ms[i]}, 10) Distribution"},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(
        active=3,
        steps=[
            dict(
                label=f"m = {m}",
                method="update",
                args=[
                    {"visible": [m == step for step in Ms]},
                    {"title": f"F({m}, 10) Distribution"},
                ],
            )
            for m in Ms
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("F_distribution_change_M.html", auto_open=True)

fig = go.Figure(layout_yaxis_range=[0, 1])

Ns = [1, 2, 3, 4, 5, 10, 20, 50, 100]

for step in Ns:
    x = np.arange(0, 10, 0.001)
    y = [F_distribution(i, 10, step) for i in x]
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            name=f"n = {step}",
            x=x,
            y=y,
        )
    )

# Make 10th trace visible
fig.data[3].visible = True
fig.update_layout(
    title="F(10, 4) Distribution",
)

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": f"F(10, {Ns[i]}) Distribution"},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(
        active=3,
        steps=[
            dict(
                label=f"n = {n}",
                method="update",
                args=[
                    {"visible": [n == step for step in Ns]},
                    {"title": f"F(10, {n}) Distribution"},
                ],
            )
            for n in Ns
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("F_distribution_change_N.html", auto_open=True)
