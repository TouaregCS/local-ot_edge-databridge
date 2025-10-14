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
