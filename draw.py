import matplotlib.pyplot as plt
import matplotlib.patches as patches
from graphviz import Digraph
import os
import html
os.environ["PATH"] += os.pathsep + 'D:/Program Files/Graphviz/bin/'

# 创建一个有向图
dot = Digraph()

# 添加代码节点
code = """
function doNothing() public { \l    uint i = 0;\l    while(i < 5) {\l        i++;\l    }\l}\l
"""

# 添加节点
dot.node('A', label=code, shape='box')
dot.node('B', 'FunctionDefinition', shape='box', style='rounded')
dot.node('C', 'ParameterList', shape='box', style='rounded')
dot.node('D', 'ParameterList', shape='box', style='rounded')
dot.node('E', 'BlockStatement', shape='box', style='rounded')
dot.node('F', 'VariableDeclarationStatement', shape='box', style='rounded')
dot.node('G', 'WhileStatement', shape='box', style='rounded')
dot.node('H', 'Literal', shape='box', style='rounded')
dot.node('I', 'VariableDeclaration', shape='box', style='rounded')
dot.node('J', 'ElementaryTypeName', shape='box', style='rounded')
dot.node('K', 'BinaryOperation', shape='box', style='rounded')
dot.node('L', 'BlockStatement', shape='box', style='rounded')
dot.node('M', 'Literal', shape='box', style='rounded')
dot.node('N', 'Identifier', shape='box', style='rounded')
dot.node('O', 'ExpressionStatement', shape='box', style='rounded')
dot.node('P', 'UnaryOperation', shape='box', style='rounded')
dot.node('Q', 'Identifier', shape='box', style='rounded')
dot.node('R', 'MemberReference', shape='box', style='rounded')
dot.node('S', 'MemberReference', shape='box', style='rounded')



# code = html.escape(code).replace('\n', '<br/>')
#dot.node('Z', label='<<font face="Courier New" color="black">{}</font>>'.format(code), shape='box')


# 添加边
dot.edges(['BC', 'BD', 'BE', 'EF', 'EG', 'FH', 'FI', 'IJ', 'GK', 'GL', 'KM', 'KN', 'LO', 'OP', 'PQ', 'QR', 'NS'])
dot.graph_attr['ranksep'] = '0.3'


# 保存或显示图表
dot.view()