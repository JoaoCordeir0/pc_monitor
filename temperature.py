import wmi

try:  
    w = wmi.WMI(namespace=r"root\wmi", privileges=["Security"])

    temperature = w.MSAcpi_ThermalZoneTemperature()[0]

    print(temperature)

    temperature = int((temperature.CurrentTemperature / 10) - 273.15)

    print(f'Temperatura: {temperature}°C')
except Exception as err:
    print(err)
finally:
    input('\nAperte qualquer tecla para sair\n')
