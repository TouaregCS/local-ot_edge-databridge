import modbus_tk
import modbus_tk.defines as defines
import modbus_tk.modbus_tcp as modbus_tcp
import time
import random

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 50202

try:
    server = modbus_tcp.TcpServer(port=SERVER_PORT, address=SERVER_HOST)
    server.start()
    print(f"PLC Simulator (modbus-tk) startuje na {SERVER_HOST}:{SERVER_PORT}...")

    slave_1 = server.add_slave(1)

    slave_1.add_block("holding_registers", defines.HOLDING_REGISTERS, 0, 100)

    temp = 60.0

    while True:
        temp += 0.5
        if temp > 80:
            temp = 60.0

        value = int(temp * 10)

        slave_1.set_values("holding_registers", 0, [value])

        print(f"Modbus HR0 aktualizovan: {temp:.1f} C")
        time.sleep(5)

except Exception as e:
    print(f"Chyba pri behu Modbus serveru {e}")

finally:
    if "server" in locals() and server.is_started():
        server.stop()
    
    print("PLC Sim zastaven.")
