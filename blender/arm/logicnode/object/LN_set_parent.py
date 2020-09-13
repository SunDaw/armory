from arm.logicnode.arm_nodes import *

class SetParentNode(ArmLogicTreeNode):
    """Set parent node"""
    bl_idname = 'LNSetParentNode'
    bl_label = 'Set Parent'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('ArmNodeSocketObject', 'Parent', default_value='Parent')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(SetParentNode, category=PKG_AS_CATEGORY, section='relations')