import random
import colorsys

import bpy



def init_vdmk2(node):

    def fold_color(color, shift):
        h, s, v = colorsys.rgb_to_hsv(*color)
        return colorsys.hsv_to_rgb(shift, s, v)

    A = [0.938000, 0.948000, 0.900000, 1.000000]
    B = [0.500000, 0.752000, 0.899000, 1.000000]
    C = [0.030100, 0.488000, 0.899000, 1.000000]

    shift = random.random()
    node.vertex_colors = fold_color(A[:3], shift)
    node.edge_colors = fold_color(B[:3], shift)
    node.face_colors = fold_color(C[:3], shift)

    node.edge_width = 1.0
    node.vertex_size = 2.0
