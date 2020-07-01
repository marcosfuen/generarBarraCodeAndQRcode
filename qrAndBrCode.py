from pygooglechart import QRChart
import qrcode
import barcode
from barcode.writer import ImageWriter
import os
import shutil


def crear_code128(valor, archivo):
    code128 = barcode.Code128(valor, writer=barcode.writer.ImageWriter())
    filename = code128.save(archivo)


def crear_ean13(valor, archivo):
    ean = barcode.get('ean13', valor, writer=barcode.writer.ImageWriter())
    filename = ean.save(archivo)


def crear_isbn13(valor, archivo):
    """ El valor de isbn13 tiene que empezar por 978 or 979"""
    isbn = barcode.ISBN13(valor, writer=barcode.writer.ImageWriter())
    filename = isbn.save(archivo)


def generarQrAndBr():
    f = open('info.txt', encoding='utf-8')
    infos = f.readlines()
    for info in infos:
        cols = info.replace(',', ' ').replace(';', '\n')
        filename = info.split(',')[0]
        filenameDir = info.split(';')[0].replace(',', ' ')
        img = qrcode.make(str(cols))
        os.mkdir(str(filenameDir))
        img.save(str(filenameDir)+"/"+"%s.png" % str(filename))
        valor = info.split(',')[2]
        # crear_code128(str(valor), str(info.split(
        #     ',')[0])+'_'+str(info.split(',')[1]))
        crear_code128(str(valor), str(filenameDir)+"/"+str(info.split(';')[0]).replace(',', ' ')+'_BarraCode')


if __name__ == "__main__":
    generarQrAndBr()
