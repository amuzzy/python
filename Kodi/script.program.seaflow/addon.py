import xbmc
import xbmcgui

# Create a window, and put the traffic gif in it
# This is just a proof of concept, and not at all production worthy.

class Traffic(xbmcgui.Window):
        def __init__(self):
               self.addControl(xbmcgui.ControlImage(10,10,1250,700, 'http://images.wsdot.wa.gov/nwflow/flowmaps/bridges.gif', aspectRatio=2))

MyWindow = Traffic()
MyWindow.doModal()

del MyWindow

