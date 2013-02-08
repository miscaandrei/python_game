import sys
from PyQt4 import QtGui, QtCore


class Raqueta(QtCore.QRect):
    vel=0
    amunt=False
    abaix=False
    
    def __init__(self, x=100, y=100):
        super(Raqueta,self).__init__(x,y,10,100)
    
    def pinta(self,qp):
        color = QtGui.QColor( 0, 0, 0 )
        color.setNamedColor( '#d4d4d4' )
        qp.setPen(color)
        qp.setBrush( QtGui.QColor(0,0,255))
        qp.drawRect(self)
        
        if (self.amunt==True):
            self.puja()
        elif (self.abaix==True):
            self.baixa()
    
    def puja(self):
        y=self.y()
        x=self.x()
        #self.setY(y-4)
        #self.moveBottom(y-4)
        #self.moveTop(y-4)
        self.moveTo(x,y-4)
    
    def baixa(self):
        y=self.y()
        x=self.x()
        #self.setY(y+4)
        #self.moveBottom(y+4)
        #self.moveTop(y+4)
        self.moveTo(x,y+4)
'''
    def detecta_colisions(self, objecte_x,objecte_y):
        col=self.contains(objecte_x,objecte_y)
        
        if (col==True):
            #print 'Xoque \n'
            self.pantalla.pilo.setVelX()
'''
