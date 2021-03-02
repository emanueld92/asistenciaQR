from django.shortcuts import render,HttpResponse

import qrcode 
# Create your views here.
def createQr(request):
    
    #creacion de objeto codigo QR
    qr=qrcode.QRCode(
        version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
    
    #crear infomacion mediante diccionario python
    info={'user':'emanueld92','email':'emanuelx92@gmail.com','cargo':'programador'}
    
    #agregar informacion
    qr.add_data(info)
    qr.make(fit=True)
    
    #creamos imagen para el objeto codigo QR
    imagen=qr.make_image()
    
    #guardamos la imagen con la estension que queremos
    
    imagen.save('user.png')
    
    return HttpResponse('exito', imagen)
