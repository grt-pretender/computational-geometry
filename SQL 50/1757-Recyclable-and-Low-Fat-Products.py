# 1757. Recyclable and Low Fat Products
# Write a solution to find the ids of products that are both low fat and recyclable.
# using Pandas

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
  ans = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')] 
  return ans[['product_id']]

