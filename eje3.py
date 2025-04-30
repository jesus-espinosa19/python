
presion = float (input("ingresar presion : "))
volumen = float (input ("ingresar volumen : "))
temperatura = float (input("ingresar temperatura : "))

masa = float(presion * volumen)/float(0.37 * float(temperatura + 460))

print(masa)
