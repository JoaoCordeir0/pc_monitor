import os
import time
import psutil

while(True):    
    cpu_use = psutil.cpu_percent(interval=1) # Get CPU usage
    nucleos = psutil.cpu_count() # Get CPU núcleos 
    memory = psutil.virtual_memory()

    batery = psutil.sensors_battery() # Get batery system

    diskUsage = psutil.disk_usage('/')

    os.system('cls')
    
    print(f'Uso atual do processador: {cpu_use}%')
    print(f'Quantidade de núcleos do processador: {nucleos}') 
    print(f'Memória instalada utilizável: {round(memory[0] / 1024 / 1024 / 1024, 2)} GB')   
    print(f'Nível da bateria: {batery[0]}%')
    print(f'Espaço em disco usado: {round(diskUsage[1] / 1024 / 1024 / 1024, 2)} GB')
    print(f'Espaço em disco livre: {round(diskUsage[2] / 1024 / 1024 / 1024, 2)} GB')

    time.sleep(2)