import tkinter as tk
from tkinter import ttk
from scapy.all import sniff, IP, TCP, UDP
import matplotlib.pyplot as plt
from collections import Counter
from database import NetworkDatabase

class NetworkTrafficAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Analyzer")

        self.start_button = ttk.Button(root, text="Começar Captura", command=self.start_capture)
        self.start_button.pack()

        self.num_packets_entry = ttk.Entry(root)
        self.num_packets_entry.pack()
        self.num_packets_entry.insert(0, "20")

        self.results_text = tk.Text(root, height=10, width=40)
        self.results_text.pack()

        self.plot_button = ttk.Button(root, text="Mostrar Gráficos", command=self.plot_graphs)
        self.plot_button.pack()

    def start_capture(self):
        num_packets = int(self.num_packets_entry.get())
        captured_ports = []
        captured_protocols = []
        captured_src_ips = []
        captured_dst_ips = []

        def packet_callback(packet):
            if IP in packet:
                protocol = None
                port = None
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst

                if TCP in packet:
                    protocol = 6  
                    port = packet[TCP].dport
                if UDP in packet:
                    protocol = 17  
                    port = packet[UDP].dport
                if protocol and port:
                    captured_ports.append(port)
                    captured_protocols.append(protocol)
                    captured_src_ips.append(src_ip)
                    captured_dst_ips.append(dst_ip)
                    self.results_text.insert(tk.END, f"Porta capturada: {port}\n")

        sniff(prn=packet_callback, count=num_packets)

        self.captured_ports = captured_ports
        self.captured_protocols = captured_protocols
        self.captured_src_ips = captured_src_ips
        self.captured_dst_ips = captured_dst_ips
        self.results_text.insert(tk.END, "Captura concluída.\n")
    def plot_graphs(self):
        db = NetworkDatabase()
        
        for i in range(len(self.captured_ports)):
            db.insert_data(self.captured_src_ips[i], self.captured_dst_ips[i], self.captured_protocols[i], self.captured_ports[i])

        db.close()

        port_counter = Counter(self.captured_ports)
        ports = list(port_counter.keys())
        counts = list(port_counter.values())

        plt.figure(figsize=(10, 5))
        plt.barh(range(len(ports)), counts, tick_label=ports)
        plt.xlabel('Qtd')
        plt.ylabel('Portas')
        plt.title('Portas Capturadas')
        plt.show()

        protocol_names = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP',
        }

        protocol_names_list = [protocol_names.get(proto, 'Other') for proto in self.captured_protocols]

        protocol_counter = Counter(protocol_names_list)
        protocols = list(protocol_counter.keys())
        protocol_counts = list(protocol_counter.values())

        plt.figure(figsize=(8, 6))
        plt.pie(protocol_counts, labels=protocols, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Distribuição de Protocolos')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkTrafficAnalyzerApp(root)
    root.mainloop()
