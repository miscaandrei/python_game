import sys
from PyQt4 import QtGui, QtCore



class Pilota():
    posx=10
    posy=10
    velx=2
    vely=2
    maxVel=0
    color=0
    tamany=15
    
    
    def pinta(self,qp):
        color = QtGui.QColor( 0, 0, 0 )
        color.setNamedColor( '#d4d4d4' )
        qp.setPen(color)
        qp.setBrush( QtGui.QColor(0,255,0))
        qp.drawEllipse( self.posx, self.posy , self.tamany, self.tamany)
    
    
    #def actualitza_pos(amplada,alcada):
    def actualitza_pos(self,amplada,alcada):
        
        self.posx=self.posx+self.velx
        self.posy=self.posy+self.vely
        
        if (self.posx>amplada-self.tamany):
            self.velx=self.velx*(-1)
        elif (self.posx<0):
            self.velx=self.velx*(-1)
        
        if (self.posy>alcada-self.tamany):
            self.vely=self.vely*(-1)
        elif (self.posy<0):
            self.vely=self.vely*(-1)
        
        
    def setVelX(self,valor):
        if (self.velx<0):
            self.velx=-valor
        else:
            self.velx=valor
    
    def setVelY(self,valor):
        if (self.vely<0):
            self.vely=-valor
        else:
            self.vely=valor
    def rebota(self):
            self.velx=self.velx*(-1)
    
    '''
    def detecta_colisions(self, objecte_x,objecte_width,objecte_y,objecte_height):
        col = False
        if (objecte_x<=self.posx<=objecte_x+objecte_width):
            col==True
        if (objecte_y<=self.posy<=objecte_y+objecte_height):
            col==True
        
        
        if (col==True):
            print 'Xoque \n'
    '''
