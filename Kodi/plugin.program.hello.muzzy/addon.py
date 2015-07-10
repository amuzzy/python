import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello Muzzy!"
line2 = "You've written your first plugin."
 
xbmcgui.Dialog().ok(addonname, line1, line2)