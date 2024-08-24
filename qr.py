import pyqrcode

def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png',scale=6)
    print('QR generted')
    
if __name__=='__main__':
    qrcode()
    
    
#Install Package :
# 1. pip install pypng
# 2. pip install pyqrcode