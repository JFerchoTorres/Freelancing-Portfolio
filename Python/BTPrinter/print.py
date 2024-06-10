import bluetooth
import bluetooth.btcommon

def discover_devices(printer_name):
    print("Searching for devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    print(f"Found {len(devices)} devices")

    for addr, name in devices:
        print(f" {addr} - {name}")
        if name==printer_name:
            return addr
    print("Bluetooth printer not found")
    return None

def print_to_bluetooth_printer(printer_address, message):
    port=1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((printer_address, port))
        sock.send(message)
        print("Message sent to printer")
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Bluetooth error {err}")
    finally:
        sock.close()


if __name__ == "__main__":
    printer_name="Epson" # write printer name
    message="Hello this is a test print"
    printer_address =  discover_devices(printer_name)
    if printer_address:
        print_to_bluetooth_printer(printer_address, message)
       

