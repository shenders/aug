

import numpy as np
import matplotlib.pyplot as plt

from raysect.core import Point2D

from cherab.core.math.mask import PolygonMask2D


AUG_WALL_OUTLINE = np.array([
    [1.670482, -0.9978656, 1.6668, -0.9992],
    [1.7247, -0.8754, 1.670482, -0.9978656],
    [1.87906, -0.6857192, 1.9389, -0.725],
    [1.876064, -0.6857951, 1.87906, -0.6857192],
    [2.012702, -0.5620515, 2.0106, -0.5599],
    [2.0748, -0.5622, 2.012702, -0.5620515],
    [1.994233, -0.5503711, 1.999922, -0.5470718],
    [1.8787, -0.6829, 1.994233, -0.5503711],
    [1.55531, -1.184098, 1.5535, -1.1878],
    [1.5553, -1.1764, 1.55531, -1.184098],
    [1.553275, -1.172173, 1.5553, -1.1764],
    [1.4629, -1.0642, 1.553275, -1.172173],
    [1.279902, -1.10069, 1.2818, -1.0964],
    [1.2799, -1.1231, 1.279902, -1.10069],
    [1.459345, -1.062389, 1.4629, -1.0642],
    [1.3256, -1.0624, 1.459345, -1.062389],
    [1.554398, -1.228433, 1.5585, -1.2265],
    [1.5535, -1.2378, 1.554398, -1.228433],
    [1.634719, -1.00676, 1.635806, -0.9953255],
    [1.6, -1.2265, 1.634719, -1.00676],
    [1.635806, -0.9953255, 1.6385, -0.9862],
    [1.643067, -0.9720708, 1.648819, -0.9573043],
    [1.6385, -0.9862, 1.643067, -0.9720708],
    [1.648819, -0.9573043, 1.658184, -0.9366102],
    [1.658184, -0.9366102, 1.6737, -0.9093],
    [1.705044, -0.8596209, 1.711498, -0.8530268],
    [1.695188, -0.8745627, 1.705044, -0.8596209],
    [1.711498, -0.8530268, 1.715497, -0.849835],
    [1.6737, -0.9093, 1.695188, -0.8745627],
    [1.277558, -1.002598, 1.234, -1.128],
    [1.2872, -0.974, 1.277558, -1.002598],
    [1.287806, -0.9569218, 1.2872, -0.974],
    [1.287213, -0.9400259, 1.287806, -0.9569218],
    [1.285352, -0.9225369, 1.287213, -0.9400259],
    [1.2824, -0.9061, 1.285352, -0.9225369],
    [1.277967, -0.8885204, 1.2824, -0.9061],
    [1.272915, -0.8732813, 1.277967, -0.8885204],
    [1.26639, -0.8574901, 1.272915, -0.8732813],
    [1.2588, -0.8422, 1.26639, -0.8574901],
    [1.250026, -0.8273394, 1.2588, -0.8422],
    [1.246589, -0.819812, 1.250026, -0.8273394],
    [1.145071, -0.6615313, 1.246589, -0.819812],
    [1.137196, -0.6579517, 1.141021, -0.6586267],
    [1.133596, -0.6592403, 1.137196, -0.6579517],
    [1.141021, -0.6586267, 1.145071, -0.6615313],
    [1.705318, -1.302917, 1.8406, -1.2399],
    [0.9897, -0.9265999, 1.051814, -1.062265],
    [2.133888, 0.5228651, 2.14, 0.525],
    [2.13, 0.517, 2.133888, 0.5228651],
    [1.051814, -1.062265, 1.1472, -1.1773],
    [1.5581, -1.3286, 1.705318, -1.302917],
    [1.715497, -0.849835, 1.7389, -0.8397],
    [1.7389, -0.8397, 1.7575, -0.8388],
    [1.7629, -0.8448, 1.7446, -0.8684],
    [1.7446, -0.8684, 1.7247, -0.8754],
    [1.07054, 0.369689, 1.0485, 0.165636],
    [1.770275, -0.8385522, 1.752099, -0.8263993],
    [1.7748, -0.8455, 1.770275, -0.8385522],
    [2.14973, -0.5465072, 2.1577, -0.5622],
    [1.2818, -1.0964, 1.3256, -1.0624],
    [1.2862, -1.1327, 1.2799, -1.1231],
    [1.4805, -1.0904, 1.3372, -1.0918],
    [1.4625, -1.1007, 1.4805, -1.0904],
    [2.0199, -0.547, 2.14973, -0.5465072],
    [2.0106, -0.5599, 2.0199, -0.547],
    [1.999922, -0.5470718, 2.007772, -0.5470718],
    [1.752099, -0.8263993, 1.876064, -0.6857951],
    [1.5585, -1.2265, 1.6, -1.2265],
    [1.234, -1.128, 1.244338, -1.142849],
    [1.117, -0.6693, 1.133596, -0.6592403],
    [1.216, -0.824, 1.117, -0.6693],
    [1.2333, -1.1544, 1.2007, -1.1215],
    [2.17009, 0.392917, 2.13, 0.517],
    [2.0062, -0.495558, 2.09721, -0.339173],
    [1.11425, 0.640699, 1.15303, 0.772624],
    [1.06979, 0.439321, 1.11425, 0.640699],
    [1.04204, 0.234971, 1.06979, 0.439321],
    [1.03117, 0.0290308, 1.04204, 0.234971],
    [1.03726, -0.177106, 1.03117, 0.0290308],
    [1.06028, -0.382044, 1.03726, -0.177106],
    [1.10006, -0.584396, 1.06028, -0.382044],
    [1.0835, -0.447697, 1.11173, -0.581599],
    [1.055, -0.244444, 1.0835, -0.447697],
    [1.04331, -0.0395379, 1.055, -0.244444],
    [1.0485, 0.165636, 1.04331, -0.0395379],
    [1.10927, 0.57124, 1.07054, 0.369689],
    [1.16444, 0.768926, 1.10927, 0.57124],
    [1.5012, 1.2003, 1.4934, 1.2064],
    [1.407, 1.1779, 1.5012, 1.2003],
    [1.2366, 0.9584, 1.1776, 0.8158],
    [1.3309, 1.0875, 1.2366, 0.9584],
    [1.509, 1.1902, 1.3309, 1.0875],
    [1.7806, 1.0852, 1.509, 1.1902],
    [2.46096, 0.415815, 2.3871, 0.613],
    [2.3871, -0.613, 2.46096, -0.415815],
    [0.9525, -0.2596, 0.9649, -0.7793],
    [0.9525, 0.2596, 0.9525, -0.2596],
    [0.9648, 0.7788, 0.9525, 0.2596],
    [1.6296, -1.2357, 1.6055, -1.2428],
    [1.3372, -1.0918, 1.2862, -1.1327],
    [1.5431, -1.1965, 1.4625, -1.1007],
    [1.5535, -1.1878, 1.5431, -1.1965],
    [1.9401, -0.7233, 1.8787, -0.6829],
    [1.978, -0.6657, 1.9401, -0.7233],
    [1.9497, -0.6471, 1.978, -0.6657],
    [2.0078, -0.5588, 1.9497, -0.6471],
    [2.007772, -0.5470718, 2.0078, -0.5588],
    [1.8697, -0.762, 1.7748, -0.8455],
    [1.901, -0.7826, 1.8697, -0.762],
    [1.9389, -0.725, 1.901, -0.7826],
    [1.7575, -0.8388, 1.7629, -0.8448],
    [1.6668, -0.9992, 1.6296, -1.2357],
    [1.5615, -1.2378, 1.5535, -1.2378],
    [1.5615, -1.2428, 1.5615, -1.2378],
    [1.6055, -1.2428, 1.5615, -1.2428],
    [1.0726, -0.68, 1.0946, -0.68],
    [1.0726, -0.705, 1.0726, -0.68],
    [1., -0.705, 1.0726, -0.705],
    [1., -0.725, 1., -0.705],
    [1.0726, -0.725, 1., -0.725],
    [1.0726, -0.76, 1.0726, -0.725],
    [1.0946, -0.76, 1.0726, -0.76],
    [1.0946, -0.68, 1.0946, -0.76],
    [1.2264, -0.8252, 1.216, -0.824],
    [1.2264, -0.9787, 1.2264, -0.8252],
    [1.2492, -0.9805, 1.2264, -0.9787],
    [1.2007, -1.1215, 1.2492, -0.9805],
    [1.244338, -1.142849, 1.2333, -1.1544],
    [1.9657, -0.874, 1.8766, -0.874],
    [2.1577, -0.5817, 1.9657, -0.874],
    [2.1577, -0.5622, 2.1577, -0.5817],
    [1.8766, -0.8637, 2.0748, -0.5622],
    [1.8766, -0.874, 1.8766, -0.8637],
    [2.18829, 0.311421, 2.17009, 0.392917],
    [2.19995, 0.228734, 2.18829, 0.311421],
    [2.20498, 0.145381, 2.19995, 0.228734],
    [2.20336, 0.0618921, 2.20498, 0.145381],
    [2.19509, -0.0212021, 2.20336, 0.0618921],
    [2.18022, -0.103373, 2.19509, -0.0212021],
    [2.15886, -0.184099, 2.18022, -0.103373],
    [2.13113, -0.262866, 2.15886, -0.184099],
    [2.09721, -0.339173, 2.13113, -0.262866],
    [2.00682, -0.5107909, 2.0062, -0.495558],
    [2.01484, -0.5237541, 2.00682, -0.5107909],
    [2.0282, -0.531099, 2.01484, -0.5237541],
    [2.6, -0.532, 2.0282, -0.531099],
    [2.6, 0.525, 2.6, -0.532],
    [2.14, 0.525, 2.6, 0.525],
    [1.11173, -0.581599, 1.10006, -0.584396],
    [1.15303, 0.772624, 1.16444, 0.768926],
    [1.8808, 0.9353, 1.9226, 0.965],
    [1.8803, 0.9274999, 1.8808, 0.9353],
    [1.9394, 0.8745, 1.8803, 0.9274999],
    [2.1329, 0.546, 1.9394, 0.8745],
    [2.2326, 0.546, 2.1329, 0.546],
    [2.2326, 0.582, 2.2326, 0.546],
    [2.054, 0.8739001, 2.2326, 0.582],
    [2.0031, 0.8745, 2.054, 0.8739001],
    [2.0031, 0.8979, 2.0031, 0.8745],
    [1.9288, 0.9646, 2.0031, 0.8979],
    [1.9226, 0.965, 1.9288, 0.9646],
    [1.4934, 1.2064, 1.5012, 1.2166],
    [1.3666, 1.1779, 1.407, 1.1779],
    [1.3219, 1.1187, 1.3666, 1.1779],
    [1.3283, 1.1138, 1.3219, 1.1187],
    [1.3204, 1.1034, 1.3283, 1.1138],
    [1.3116, 1.1083, 1.3204, 1.1034],
    [1.1313, 0.8692001, 1.3116, 1.1083],
    [1.1417, 0.8612999, 1.1313, 0.8692001],
    [1.1194, 0.8316, 1.1417, 0.8612999],
    [1.1601, 0.8009999, 1.1194, 0.8316],
    [1.1671, 0.8019, 1.1601, 0.8009999],
    [1.1776, 0.8158, 1.1671, 0.8019],
    [1.7734, 1.08, 1.7806, 1.0852],
    [1.7723, 1.073, 1.7734, 1.08],
    [1.8651, 0.9458, 1.7723, 1.073],
    [1.872, 0.9447, 1.8651, 0.9458],
    [1.9129, 0.9734, 1.872, 0.9447],
    [1.9141, 0.9805, 1.9129, 0.9734],
    [1.8361, 1.0874, 1.9141, 0.9805],
    [1.8104, 1.0967, 1.8361, 1.0874],
    [1.8093, 1.1045, 1.8104, 1.0967],
    [1.5012, 1.2166, 1.8093, 1.1045],
    [1.7053, 1.3029, 1.5581, 1.3286],
    [1.8407, 1.2399, 1.7053, 1.3029],
    [2.0097, 1.1144, 1.8407, 1.2399],
    [2.1591, 0.9659, 2.0097, 1.1144],
    [2.2858, 0.7977, 2.1591, 0.9659],
    [2.3871, 0.613, 2.2858, 0.7977],
    [2.50591, 0.210064, 2.46096, 0.415815],
    [2.521, 0., 2.50591, 0.210064],
    [2.50591, -0.210063, 2.521, 0.],
    [2.46096, -0.415815, 2.50591, -0.210063],
    [2.233, -0.884, 2.3871, -0.613],
    [2.233, -1.12, 2.233, -0.884],
    [2.0097, -1.12, 2.233, -1.12],
    [1.8406, -1.2399, 2.0097, -1.12],
    [1.4094, -1.3152, 1.5581, -1.3286],
    [1.2692, -1.2636, 1.4094, -1.3152],
    [1.1472, -1.1773, 1.2692, -1.2636],
    [0.9649, -0.7793, 0.9897, -0.9265999],
    [0.9897, 0.9265999, 0.9648, 0.7788],
    [1.2692, 1.2636, 1.1472, 1.1773],
    [1.4094, 1.3152, 1.2692, 1.2636],
    [1.5581, 1.3286, 1.4094, 1.3152],
    [1.1472, 1.1773, 1.0519, 1.0624],
    [1.0519, 1.0624, 0.9897, 0.9265999]
])


AUG_WALL_POLYGON_BOUNDARY = [
    Point2D(1.0566, -0.072559),
    Point2D(1.0647, -0.20806),
    Point2D(1.0761, -0.31002),
    Point2D(1.0902, -0.41073),
    Point2D(1.112, -0.51051),
    Point2D(1.1403, -0.61459),
    Point2D(1.2011, -0.73543),
    Point2D(1.2578, -0.83796),
    Point2D(1.2736, -0.87249),
    Point2D(1.2828, -0.90526),
    Point2D(1.2873, -0.93967),
    Point2D(1.2881, -0.96552),
    Point2D(1.283, -0.98849),
    Point2D(1.2728, -1.0185),
    Point2D(1.2619, -1.0499),
    Point2D(1.251, -1.0812),
    Point2D(1.2402, -1.1124),
    Point2D(1.2396, -1.135),
    Point2D(1.2534, -1.1306),
    Point2D(1.2719, -1.1075),
    Point2D(1.2923, -1.0873),
    Point2D(1.3143, -1.0702),
    Point2D(1.3422, -1.0617),
    Point2D(1.3758, -1.0616),
    Point2D(1.4092, -1.0616),
    Point2D(1.4427, -1.0616),
    Point2D(1.4615, -1.0625),
    Point2D(1.4734, -1.0764),
    Point2D(1.4951, -1.1031),
    Point2D(1.5186, -1.1305),
    Point2D(1.5422, -1.1581),
    Point2D(1.5541, -1.18),
    Point2D(1.549, -1.1924),
    Point2D(1.5514, -1.2113),
    Point2D(1.5792, -1.2259),
    Point2D(1.6016, -1.2124),
    Point2D(1.6058, -1.1852),
    Point2D(1.6101, -1.1577),
    Point2D(1.6144, -1.1302),
    Point2D(1.6188, -1.1028),
    Point2D(1.6231, -1.0753),
    Point2D(1.6275, -1.0478),
    Point2D(1.6318, -1.0204),
    Point2D(1.6359, -0.99632),
    Point2D(1.643, -0.97151),
    Point2D(1.6606, -0.93297),
    Point2D(1.678, -0.88738),
    Point2D(1.6943, -0.85223),
    Point2D(1.724, -0.82679),
    Point2D(1.8048, -0.74573),
    Point2D(1.9304, -0.58206),
    Point2D(2.0387, -0.40998),
    Point2D(2.1005, -0.29483),
    Point2D(2.1308, -0.21865),
    Point2D(2.1624, -0.0994),
    Point2D(2.1843, 0.021977),
    Point2D(2.1892, 0.10393),
    Point2D(2.1875, 0.18615),
    Point2D(2.1682, 0.26597),
    Point2D(2.1427, 0.34388),
    Point2D(2.1147, 0.44271),
    Point2D(2.0585, 0.59552),
    Point2D(1.9744, 0.77719),
    Point2D(1.8939, 0.90038),
    Point2D(1.8123, 1.0016),
    Point2D(1.6998, 1.0947),
    Point2D(1.5727, 1.1482),
    Point2D(1.4254, 1.1258),
    Point2D(1.2954, 1.0138),
    Point2D(1.2176, 0.85603),
    Point2D(1.1606, 0.69749),
    Point2D(1.1139, 0.53477),
    Point2D(1.0745, 0.33447),
    Point2D(1.0553, 0.13117),
]


def plot_aug_wall_outline(style='k'):

    for i in range(AUG_WALL_OUTLINE.shape[0]):
        plt.plot([AUG_WALL_OUTLINE[i, 0], AUG_WALL_OUTLINE[i, 2]],
                 [AUG_WALL_OUTLINE[i, 1], AUG_WALL_OUTLINE[i, 3]], style)

    plt.axis('equal')


def plot_wall_segment(list_element):
    plt.plot([list_element[0], list_element[2]], [list_element[1], list_element[3]], 'r')


def get_aug_wall_mask():

    n = len(AUG_WALL_POLYGON_BOUNDARY)
    wall_points = np.zeros((n, 2))

    for i in range(n):
        wall_points[i, 0] = AUG_WALL_POLYGON_BOUNDARY[i].x
        wall_points[i, 1] = AUG_WALL_POLYGON_BOUNDARY[i].y

    return PolygonMask2D(wall_points)
