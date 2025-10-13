from pyModbusTCP.client import ModbusClient
import paho.mqtt.client as mqtt
import json
import time

# Modbus PLC konfigurace
PLC_HOST = "127.0.0.1"
PLC_PORT = 50202
MODBUS_REGISTER = 0  # Holding Register kde je teplota (HR0)

# MQTT konfigurace
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "ot/factory01/motor/temp_raw"

# Inicializace Modbus Clienta
modbus_client = ModbusClient(host=PLC_HOST, port=PLC_PORT, auto_open=True, auto_close=True)

# Inicializace MQTT Clienta
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)

print("Edge Gateway spusten. Data z PLC posila na MQTT...")

try:
    while True:
        # Data z PLC pres Modbus
        registers = modbus_client.read_holding_registers(MODBUS_REGISTER, 1)
        
        if registers:
            # Prevedeni celych cisel (int) zpet na desetinna (float)
            raw_temp_int = registers[0]
            actual_temp = raw_temp_int / 10.0

            # Vytvoreni JSON zpravy pro odeslani do MQTT
            payload = {
                "timestamp": time.time(),
                "device_id": "motor-001",
                "temperature": actual_temp,
                "unit": "C"
            }

            # Zprava na MQTT Broker
            mqtt_client.publish(MQTT_TOPIC, json.dumps(payload))
            print(f"MQTT OUT: {actual_temp:.1f}C | Topic: {MQTT_TOPIC}")
        else:
            print("Chyba cteni Modbus Registru.")

        time.sleep(5)  # Cteni kazdych 5 sekund

except KeyboardInterrupt:
    print("\nEdge Gateway zastaven uzivatelem.")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
                        
            
