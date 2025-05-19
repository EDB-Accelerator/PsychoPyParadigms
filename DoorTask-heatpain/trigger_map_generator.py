import pandas as pd
from itertools import product
import ace_tools as tools

def trigger_number(r, p, e):
    return (e - 1) * 7 ** 2 + (p - 1) * 7 + (r - 1)

# build rows
rows = [
    {
        "generated_number": trigger_number(r, p, e),
        "r": r,
        "p": p,
        "e": e
    }
    for r, p, e in product(range(1, 8), range(1, 8), range(1, 6))
]

df = pd.DataFrame(rows)

# save to CSV
file_path = "trigger_map.csv"
df.to_csv(file_path, index=False)

# show interactive table
tools.display_dataframe_to_user("Trigger Number Map", df)
