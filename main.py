import pandas as pd
import datetime

d = datetime.datetime.now(datetime.UTC)
url = (f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/"
       f"focos_10min_{d.strftime('%Y%m%d_%H')}{(d.minute // 10 * 10):02d}.csv")

try:
    df = pd.read_csv(url)
    df.to_csv("queimadas.csv", mode='a', header=not pd.io.common.file_exists("queimadas.csv"), index=False)
    print("CSV atualizado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar ou salvar CSV: {e}")
