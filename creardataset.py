import psutil
import pandas as pd
import time

# Primera llamada para inicializar el cálculo de CPU
for proc in psutil.process_iter():
    try:
        proc.cpu_percent(interval=None)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

# Esperar un segundo para que el sistema "respire"
time.sleep(1)

# Ahora recolectamos los datos reales
process_data = []
for proc in psutil.process_iter(attrs=["pid", "name", "username", "cpu_percent", "memory_percent"]):
    try:
        info = proc.info
        process_data.append(info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

# Guardar a CSV
df = pd.DataFrame(process_data)
df.to_csv("procesos_activos.csv", index=False)
print("Archivo actualizado con valores reales de uso de CPU.")

