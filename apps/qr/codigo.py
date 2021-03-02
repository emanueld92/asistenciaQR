import qrcode  # Importamos el modulo necesario para trabajar con codigos QR

imagen = qrcode.make('hola vero desde codigo QR')  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('codigo.png', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()