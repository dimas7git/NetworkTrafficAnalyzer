# Network Traffic Analyzer

Este é um pequeno aplicativo Python para capturar tráfego de rede, analisar os protocolos e portas capturados e exibir gráficos.

## Pré-requisitos

- Python 3.x

## Instalação

1. Clone este repositório para o seu sistema local:

```bash
git clone https://github.com/dimas7git/NetworkTrafficAnalyzer
```
2. Navegue até o diretório do projeto
   
```bash
cd NetworkTrafficAnalyzer
```
3. Instale as dependências usando o pip3
   
```bash
pip3 install scapy matplotlib
pip3 install sqlite3
```

## Uso
### Capturando e Analisando Tráfego de Rede
1. Abra um terminal e navegue até o diretório do projeto.
2. Execute o script abaixo para iniciar a captura e análise de tráfego:

```bash
python sniff.py
```
3. Insira o número de pacotes que deseja capturar no campo de entrada correspondente.
4. Clique no botão "Começar Captura" para iniciar a captura de pacotes.
5. Após a captura, você verá informações sobre as portas capturadas e os protocolos na janela de resultados.

### Visualizando Gráficos
1. Após a captura, clique no botão "Mostrar Gráficos" para visualizar os gráficos gerados.

## Arquivos
1. sniff.py: Script principal para captura e análise de tráfego de rede.
2. database.py: Script para interagir com o banco de dados SQLite onde os dados capturados são armazenados.
3. network_traffic.db: é criado e gerenciado pelo script database.py. Ele armazena os seguintes campos para cada pacote capturado:
```bash
src_ip: O endereço IP de origem do pacote.
dst_ip: O endereço IP de destino do pacote.
protocol: O protocolo associado ao pacote (TCP, UDP, ICMP, etc.).
port: A porta associada ao pacote (se aplicável).
```
