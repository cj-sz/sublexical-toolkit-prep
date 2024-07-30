import pandas as pd

df = pd.read_csv("cmu_ipa_cambridge.csv")

f_df = df[len(df['CMU IPAs']) > 0 & len(df['Cambridge IPAs']) > 0 & len(df['Matched Pronunciations (Toolkit)']) == 0]
print(f_df.shape)