import psutil
import pandas as pd

# Recolectar procesos activos
process_data = []
for proc in psutil.process_iter(attrs=["pid", "name", "username", "cpu_percent", "memory_percent"]):
    try:
        info = proc.info
        process_data.append(info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

# Convertir a DataFrame
df = pd.DataFrame(process_data)
df.to_csv("procesos_activos.csv", index=False)
print("Archivo procesos_activos.csv generado con éxito.")
