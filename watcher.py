import pandas as pd
from cryptosight.utils import fetch_transactions
from cryptosight.patterns import detect_anomalies, plot_behavior

class WalletWatcher:
    def __init__(self, address, network):
        self.address = address
        self.network = network

    def analyze(self):
        print(f"[+] Получаем транзакции для {self.address}...")
        txs = fetch_transactions(self.address)

        if not txs or txs.empty:
            print("[-] Транзакции не найдены.")
            return

        print(f"[+] Обработка {len(txs)} транзакций...")
        anomalies = detect_anomalies(txs)
        print(f"[!] Найдено аномалий: {len(anomalies)}")
        print(anomalies[["hash", "value_eth", "time_diff", "cluster"]])

        print("[+] Визуализация поведения...")
        plot_behavior(txs, anomalies)
