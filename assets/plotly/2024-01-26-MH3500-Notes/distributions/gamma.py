import plotly.graph_objects as go
import numpy as np
import math


def gamma_distribution(x, alpha=2, beta=1):
    if x <= 0:
        return 0
    else:
        return (x ** (alpha - 1) * np.exp(-x / beta)) / (
            beta**alpha * math.gamma(alpha)
        )


fig = go.Figure(layout_yaxis_range=[0, 1])

alphas = np.arange(0.5, 5, 0.1)

for step in alphas:
    x = np.arange(0, 10, 0.001)
    y = [gamma_distribution(i, step, 1) for i in x]
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            name="α = " + str(step),
            x=x,
            y=y,
        )
    )

# Make 10th trace visible
fig.data[10].visible = True
fig.update_layout(
    title="Gamma Distribution (α = 1.5, β = 1)",
)

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": "α = {:.1f}".format(float(alphas[i]))},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(
        active=10,
        steps=[
            dict(
                label="α = {:.1f}".format(alpha),
                method="update",
                args=[
                    {"visible": [alpha == step for step in alphas]},
                    {"title": "Gamma Distribution (α = {:.1f}, β = 1)".format(alpha)},
                ],
            )
            for alpha in alphas
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("gamma_distribution_change_alpha.html", auto_open=True)

fig = go.Figure(layout_yaxis_range=[0, 0.8])

betas = np.arange(0.5, 5, 0.1)

for step in betas:
    x = np.arange(0, 10, 0.001)
    y = [gamma_distribution(i, 2, step) for i in x]
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            name="β = " + str(step),
            x=x,
            y=y,
        )
    )

# Make 10th trace visible
fig.data[10].visible = True
fig.update_layout(
    title="Gamma Distribution (α = 2, β = 1)",
)

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": "β = {:.1f}".format(float(betas[i]))},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(
        active=10,
        steps=[
            dict(
                label="β = {:.1f}".format(beta),
                method="update",
                args=[
                    {"visible": [beta == step for step in alphas]},
                    {"title": "Gamma Distribution (α = 2, β = {:.1f})".format(beta)},
                ],
            )
            for beta in betas
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("gamma_distribution_change_beta.html", auto_open=True)
