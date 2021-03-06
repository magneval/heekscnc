from Operation import Operation
import HeeksCNC

class Profile(Operation):
    def __init__(self):
        Operation.__init__(self)

    def TypeName(self):
        return "Profile"

    def op_icon(self):
        # the name of the PNG file in the HeeksCNC icons folder
        return "profile"

    def get_selected_sketches(self):
        return 'hi'

    def Edit(self):
        import wxProfile
        class wxProfiledlg( wxProfile.Profiledlg ):
            def __init__( self, parent ):
                wxProfile.Profiledlg.__init__( self, parent )

            def CloseWindow(self,event):
                self.Destroy()


        dlg = wxProfiledlg(None)
        dlg.Show(True)
