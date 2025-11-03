# Lokální OT Datový Most (On-Premise Lab)
![GitHub License](https://img.shields.io/github/license/TouaregCS/local-ot_edge-databridge)  ![GitHub repo size](https://img.shields.io/github/repo-size/TouaregCS/local-ot_edge-databridge)  [![Bandit](https://github.com/TouaregCS/local-ot_edge-databridge/actions/workflows/bandit.yml/badge.svg)](https://github.com/TouaregCS/local-ot_edge-databridge/actions/workflows/bandit.yml)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  



Cíl: Vytvoření izolovaného virtualizovaného řetězce pro simulaci průmyslového provozu, sběr dat, monitoring a detekci v lokálním prostředí, bez závislosti na cloudu. OS Linux Mint

Plně funkční Lokální OT/Edge Kanál s využitím Python scriptů a knihoven, s jednoduchou architekturou: Modbus -> Python Edge -> MQTT Broker.

## Konfigurace a scripty

Pro celý projekt si vytvoříme novou složku (např. local-on-premise-lab), ve které uložíme scripty a budeme zpouštět terminály. 

  ### [Instalační scripty (Bash)](Install_scripts.md)
	   Instalace klíčových komponent pro projekt (Mosquitto, Python knihovny).
  ### [plc_sim.py (Python)](plc_sim.py)
	   Simulace PLC. Script bude generovat virtuální fiktivní OT data a vysílat je pomocí protokolu Modbus/TCP.
  ### [edge_gateway.py (Python)](edge_gateway.py)
	   Script pro načítání dat přes Modbus z PCL a přeposílání na Mosquitto Broker protokolem MQTT.
  ### [Mosquitto (Bash)](mosquitto.md)
	   Spouštění, konfigurace a sledování dat MQTT Brokeru.

## Spuštění
Aktivujeme virtuální prostředí (venv)

Script, který má simulovat PLC (plc_sim.py) spustíme v jednom terminálu.

V druhém terminálu spustíme Edge Gateway (edge_gateway.py). Načítá data z PLC a posílá je do Mosquitto Brokeru.

Ve třetím terminálovém okně spustíme simulaci sledování dat z Mosquitto (Bash).

Pokud vše funguje jak má, měli bychom pozorovat dynamicky aktualizované hodnoty ve všech třech terminálech. Zprovozněný lokální hybridní kanál tak může začít sloužit k cvičení scénařů incidentů.
