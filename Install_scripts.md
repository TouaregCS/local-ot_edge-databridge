# Instalační skripty

Začneme instalací Mosquitto, bychom mohli použít protokol MQTT pro centrální datový hub.
~~~bash
# Aktualizace seznamu balíčků
sudo apt update

# Instalace Mosquitto Brokeru a klientských nástrojů 
sudo apt install mosquitto mosquitto-clients
~~~

Nyní můžeme Mosquitto povolit, spustit a zkontrolovat, že běží.
~~~bash
# Povolení automatického spuštění při startu systému
sudo systemctl enable mosquitto

# Spuštění služby
sudo systemctl start mosquitto

# Ověření, že služba běží (active/running)
sudo systemctl status mosquitto

~~~

Vytvoříme virtuální prostředí
~~~bash
python3 -m venv venv
~~~

Pokračujeme aktivací virtuálního prostředí (venv)
~~~bash
source venv/bin/activate
~~~

Ověříme instalaci balíčku modbus
~~~bash
pip list | grep modbus
~~~

Správně by se měly zobrazit knihovny ```modbus-tk``` a ```pyModbusTCP```. 
Pokud ne, musíme balíčky doinstalovat.
~~~bash
pip install modbus-tk
pip install pyModbusTCP paho-mqtt
~~~
