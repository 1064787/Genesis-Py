# Genesis-Py v0.0.3a
# Nandi, 1064787

import os
import wx
APP_EXIT = 1

name = 'GenesisPy_v0.0.1a' # GenesisPy version name

class App_Main_Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(App_Main_Frame, self).__init__(*args, **kwargs)
        
        self.InitUI()


    def InitUI(self):
        menubar = wx.MenuBar()
        toolbar = self.CreateToolBar()

        ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(panel, label="Panel Test")
        sizer.Add(text, pos = (0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        text_ctl = wx.TextCtrl(panel)
        sizer.Add(text_ctl, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOK = wx.Button(panel, label="Ok", size=(90,28))
        sizer.Add(buttonOK, pos=(3,3))
        buttonClose = wx.Button(panel, label="Close", size=(90,28))
        sizer.Add(buttonClose, pos=(3,4), flag=wx.RIGHT|wx.BOTTOM, border=10)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)

        ###Toolbar###
        main_tool_bar = toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('test.bmp'))
        toolbar.Realize() # Obligatory method to Windows

        self.Bind(wx.EVT_TOOL, self.OnQuit, main_tool_bar)
        
        #main_tool_bar.AddSeparator

        ###Menus and Submenus###
        Main_Menu = wx.Menu()
        quit_menu_item = wx.MenuItem(Main_Menu, APP_EXIT, '&Quit\tCtrl+Q')
        quit_menu_item.SetBitmap(wx.Bitmap('test.bmp'))
        Main_Menu.Append(wx.ID_NEW, '&New')
        Main_Menu.Append(wx.ID_OPEN, '&Open')
        Main_Menu.Append(wx.ID_SAVE, '&Save')

        Main_Menu.AppendSeparator

        sub_menu = wx.Menu()
        sub_menu.Append(wx.ID_ANY, '&Import')

        Main_Menu.Append(wx.ID_ANY, '&Import', sub_menu)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(Main_Menu, '&Menu')
        Main_Menu.Append(quit_menu_item)
        self.SetMenuBar(menubar)

        self.SetSize((800, 600))
        self.SetTitle(name)
        self.Centre

    def OnQuit(self, e):
        self.Close()
        

def main():
    app = wx.App()
    ex = App_Main_Frame(None)
    ex.Show()
    app.MainLoop()
    

if __name__ == '__main__':
    main()
