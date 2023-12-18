import gdown
import pandas as pd

url = 'https://drive.google.com/uc?id=1vdVe6BWLtdzkpUFKlxufGCplNyy2laVG'
output = 'tweets.csv'
gdown.download(url, output, quiet=False)

# Read the CSV file
df = pd.read_csv(output)

print(df.info())
