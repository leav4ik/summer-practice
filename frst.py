import numpy as np
import json
from pathlib import Path

script_dir = Path(__file__).parent.resolve()

output_folder = script_dir / "results"
output_folder.mkdir(exist_ok=True)

file_path = output_folder / "data.json"

A = -0.25


def f(x):
    sum1 = sum(i * np.cos((i + 1) * x + i) for i in range(1, 6))
    sum2 = sum(i * np.cos((i + 1) * A + i) for i in range(1, 6))
    return sum1 * sum2


x_val = np.arange(-10, 10.01, 0.01)

y_val = [f(x) for x in x_val]

data = [{"x": float(x), "y": float(y)} for x, y in zip(x_val, y_val)]

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump({"data": data}, file, indent=4, ensure_ascii=False)
