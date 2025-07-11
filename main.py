import os
import datetime
import pandas as pd


def main():
    current_timestamp = get_current_timestamp()
    last_timestamp = get_last_timestamp()

    if current_timestamp == last_timestamp:
        return

    d = datetime.datetime.now(datetime.UTC)
    url = (f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/"
        f"focos_10min_{current_timestamp}.csv")

    try:
        df = pd.read_csv(url)
        file_exists = os.path.exists('queimadas.csv')
        df.to_csv('queimadas.csv', mode='a', header=not file_exists, index=False)
        save_timestamp(current_timestamp)
    except Exception as e:
        print(f"Erro: {str(e)}")


def get_current_timestamp():
    d = datetime.datetime.now(datetime.UTC)
    return f"{d.strftime('%Y%m%d_%H')}{(d.minute // 10 * 10):02d}"


def get_last_timestamp():
    if os.path.exists('.timestamp'):
        with open('.timestamp', 'r') as f:
            return f.read().strip()
    return None


def save_timestamp(timestamp):
    with open('.timestamp', 'w') as f:
        f.write(timestamp)


if __name__ == '__main__':
    main()
