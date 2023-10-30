# 595. Big Countries
# Write a solution to find the name, population, and area of the big countries.
# A country is big if:
# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).

# using Pandas

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    ans = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return ans[['name', 'population', 'area']]