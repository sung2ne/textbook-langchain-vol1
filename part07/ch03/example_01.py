import pandas as pd

# CSV 로드
df = pd.read_csv("products.csv")

print(df.head())
print(f"\n총 {len(df)}개 데이터")
