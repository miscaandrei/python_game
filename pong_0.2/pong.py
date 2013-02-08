#!/usr/bin/python
# -*- coding: utf-8 -*-
#include <QTimer>
"""
1 - Timer -> print    FET
2. Avançar Pilota     FET
3. Objecte Pilota
4. Rebotar



"""
from class_Pilota import Pilota
from class_Raqueta import Raqueta
import sys
from PyQt4 import QtGui, QtCore


class Pantalla(QtGui.QWidget):
    posx = 0
    posy = 0
    radx = 5
    rady = 5
    temps = 0
    pilo=0
    #width = baseSize().width() + i * sizeIncrement().width();
    def __init__(self):
        # ULL: cridar el constructor de la classe base és IMPRESCINDIBLE
        # (si sobreescrivim el constructor __init__, si no, no cal)
        super(QtGui.QWidget,self).__init__()
        self.initUI()
 
    def initUI(self):
        # inicialitzem aqui si tenim objectes interns
        self.pilo=Pilota()
        self.raqueta_1=Raqueta()
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QtGui.QColor( 0, 0, 0 ))
        self.setPalette(pal)
        self.setAutoFillBackground(True)
        
        self.timer=QtCore.QTimer(self)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.repaint)
        
    # la funció paintEvent es crida cada cop que es pinta la pantalla
    # no cal cap connect(), ja ve connectada per la QApplication
    
    
    def paintEvent(self,e):
        # podriem liar-nos a pintar aquí mateix, o examinar l'event "e"
        # anem al lio...
        self.pinta()
    
    def pinta(self):
        qp = QtGui.QPainter()
        qp.begin(self)
        
        #primer actualitzem la posicio de la pilota 
        self.pilo.actualitza_pos(self.width(),self.height())
        
        #self.raqueta_1.detecta_colisions(self.pilo.posx,self.pilo.posy)
        self.detecta_colisions()
        
        self.pilo.pinta(qp)
        self.raqueta_1.pinta(qp)
        #i despres pintem la pilota
        
        qp.end()
    
    
    def detecta_colisions(self):
        col=self.raqueta_1.contains(self.pilo.posx,self.pilo.posy)
        
        if (col==True):
            #print "Xoque!!!! \n"
            self.pilo.rebota()



class Principal(QtGui.QWidget):
    
    def __init__(self):
        super(Principal, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.pantalla = Pantalla()
        self.pantalla.setStyleSheet('QTabBar::tab {background-color: red;}')
        
        sortirButton = QtGui.QPushButton("Surtida")
        x_slider=QtGui.QSlider(QtCore.Qt.Horizontal, self)
        x_lcd = QtGui.QLCDNumber(self)
        
        x_slider.valueChanged.connect(x_lcd.display)
        x_slider.valueChanged.connect(self.pantalla.pilo.setVelX)
        
        y_slider=QtGui.QSlider(QtCore.Qt.Vertical, self)
        y_lcd = QtGui.QLCDNumber(self)
        
        y_slider.valueChanged.connect(y_lcd.display)
        y_slider.valueChanged.connect(self.pantalla.pilo.setVelY)
        
        
        bottomBox = QtGui.QGridLayout()
        
        bottomBox.addWidget(y_lcd,0,0)
        bottomBox.addWidget(y_slider,1,0)
        bottomBox.addWidget(self.pantalla,0,1,2,2) # (fila, columna, expasio , expansio)
        bottomBox.addWidget(sortirButton,2,0)
        bottomBox.addWidget(x_slider,2,1)
        bottomBox.addWidget(x_lcd,2,2)
        
        self.setLayout(bottomBox)   
        
        self.setGeometry(300, 300, 500, 500) # posicio pantalla,algo,amplada,alçada
        self.setWindowTitle('Finestra 1') 
        self.show()
        self.setFocus()
        self.pantalla.timer.start()
        self.pantalla.pilo.posy=0
        #print self.pantalla.timer.isActive()
        #print self.pantalla.timer.interval()
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_A:
            self.pantalla.raqueta_1.amunt=True
        elif e.key() == QtCore.Qt.Key_Z:
            self.pantalla.raqueta_1.abaix=True
    
    def keyReleaseEvent(self, e):
        if not e.isAutoRepeat():
            if e.key() == QtCore.Qt.Key_A:
                self.pantalla.raqueta_1.amunt=False
            elif e.key() == QtCore.Qt.Key_Z:
                self.pantalla.raqueta_1.abaix=False


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
