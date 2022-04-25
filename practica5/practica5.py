import base64 as b64
import io
import PIL.Image as Image
archivoA=open('mystery_img1.txt','r')
archivoB=open('encoded_msg.b64','r')
resultado=open('resultado.txt','w')
cosa=archivoB.read()
imagen=archivoA.read()
decodificado=b64.b64decode(cosa)
d=decodificado.decode("utf-8")
imagenD=b64.b64decode(imagen)
resultado.write(str(d))
img= Image.open(io.BytesIO(imagenD))
img.show()
resultado.close()
archivoA.close()
archivoB.close()