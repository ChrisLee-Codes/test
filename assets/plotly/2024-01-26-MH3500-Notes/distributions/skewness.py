import plotly.graph_objects as go
import numpy as np
import math
from scipy.stats import skew


def get_distributions():
    normal = np.random.normal(0, 1, 10000)
    data = []
    for i in range(9, 0, -1):
        # now_data = np.power(normal, (2 * i + 1) / 5)
        # now_data = normal * i
        now_data = -np.exp(normal * i / 10)
        data.append({"data": now_data, "skewness": skew(now_data), "i": i})
        print("skewness = ", skew(now_data))
    for i in range(1, 10):
        # now_data = np.power(normal, (2 * i + 1) / 5)
        # now_data = normal * i
        now_data = np.exp(normal * i / 10)
        data.append({"data": now_data, "skewness": skew(now_data), "i": i})
        print("skewness = ", skew(now_data))
    return data


def get_title(data):
    title = "Skewness = %.2f" % data["skewness"]
    # title = f"i = {data['i']}"
    return title


fig = go.Figure()

data = get_distributions()

for now_data in data:
    fig.add_trace(
        go.Histogram(
            visible=False,
            x=now_data["data"],
            name=get_title(now_data),
            histnorm="probability",
            bingroup=1,
        )
    )

fig.data[9].visible = True
fig.update_layout(
    title=get_title(data[9]),
)


# Create and add slider
steps = []
for i in range(len(data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": get_title(data[i])},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)


sliders = [
    dict(
        active=9,
        steps=[
            dict(
                label=get_title(data[n]),
                method="update",
                args=[
                    {"visible": [n == i for i in range(len(data))]},
                    {"title": get_title(data[n])},
                ],
            )
            for n in range(len(data))
        ],
    )
]

fig.update_layout(sliders=sliders)

fig.write_html("skewness.html", auto_open=True)

fig = go.Figure()
