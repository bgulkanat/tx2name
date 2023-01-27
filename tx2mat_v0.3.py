#created by Baransel CG.
#www.baranselgulkanat.com
# v0.3 prefix/suffix option UI added.
# This scripts renames material names according to the their texture names 
# and can add prefix/suffix to it.
# just copy this to script editor and save it to the shelf.
import maya.cmds as cmds
windowName = 'myWindow'
if cmds.window(windowName, exists=True):
    cmds.deleteUI(windowName)
cmds.window(windowName, width=240, title='b-CG tx2mat')
cmds.columnLayout(adj=True)
cmds.text( label='Enjoy! :)', height = 15  )
cmds.separator(height = 10, style='in')
cmds.text( label='Just Rename or Include Prefix/Suffix', height = 15, bgc = (1,1,0))
cmds.separator(height = 5, style='none')
textfield = cmds.textField(enable=False)
checkbox = cmds.checkBox(label="Enable Prefix/Suffix", onCommand=lambda *args: cmds.textField(textfield, edit=True, enable=True), offCommand=lambda *args: cmds.textField(textfield, edit=True, enable=False))
def on_button_clicked(*args):
    allMaterials = cmds.ls(materials=True)
    text = cmds.textField(textfield, query=True, text=True)
    for material in allMaterials:
        file_node = cmds.listConnections(material, type="file")
        if file_node:
            file_path = cmds.getAttr(file_node[0] + ".fileTextureName")
            if file_path.count("\\"):
                file_name = file_path.split("\\")[-1]
            else:
                file_name = file_path.split("/")[-1]
                texture_name = file_name.split(".")[0]
            try:
                if not cmds.textField(textfield, query=True, enable=True):
                    cmds.rename(material,texture_name)
                else:
                    if not text:
                        cmds.warning("please fill the blank or uncheck checkbox")
                    else:
                        if cmds.radioButton('prefix', q=True, select=True):
                            if textfield:
                                cmds.rename(material,text + "_" + texture_name)
                        else:
                            if textfield:
                                cmds.rename(material,texture_name + "_" + text )
            except:
                cmds.warning("Cannot rename " + material + " because it is a read-only node")
                continue
cmds.radioCollection()
cmds.rowLayout( numberOfColumns=2, adj = 1)
cmds.radioButton('prefix', select=True)
cmds.radioButton('suffix')
cmds.setParent('..')
cmds.button(label='RenameMats!', command=on_button_clicked)
cmds.separator(height = 10, style='in')
cmds.text( label=' by <a href="https://baranselgulkanat.com" style=\"color:grey\">  Baransel </a>', hl = True, align='center')
cmds.text( label='v0.3', align='right', font = "smallObliqueLabelFont")
cmds.window(windowName, e=True, width=240, height=130)
cmds.showWindow(windowName)
