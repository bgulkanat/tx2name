import maya.cmds as cmds
allMaterials = cmds.ls(materials=True)
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
      cmds.rename(material,"M_" + texture_name)
    except:
      print("Cannot rename " + material + " because it is a read-only node")
