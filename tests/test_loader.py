from utils.data_loader import load_transactions

df = load_transactions()

print(df.head())

print()

print(df.shape)