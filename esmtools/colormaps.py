"""
Simply a bunch of NCL colormaps. Most of this script is constant colormap
arrays and then one simple function to load them.

- `load_cmap` : Function to load in a non-matplotlib/cmocean colormap.

"""
import numpy as np
from .vis import *
import pandas as pd
import matplotlib.colors as color

def load_cmap(name):
    """
    Returns a colormap to use in plotting.

    Parameters
    ----------
    name : str
        Identifier for colormap.
    """
    df = pd.DataFrame(eval(name))
    cmap = color.ListedColormap(df.values)
    return cmap

# COLORMAPS

# Sequential
# ---------

# 1. cools
cools = np.array([[ 1.        ,  1.        ,  1.        ],
       [ 0.92941176,  0.98039216,  0.76078431],
       [ 0.80392157,  1.        ,  0.80392157],
       [ 0.6       ,  0.94117647,  0.69803922],
       [ 0.3254902 ,  0.74117647,  0.62352941],
       [ 0.19607843,  0.65098039,  0.58823529],
       [ 0.19607843,  0.58823529,  0.70588235],
       [ 0.01960784,  0.43921569,  0.69019608],
       [ 0.01960784,  0.31372549,  0.54901961],
       [ 0.03921569,  0.12156863,  0.58823529],
       [ 0.17254902,  0.00784314,  0.2745098 ],
       [ 0.41568627,  0.17254902,  0.35294118]])

# 2. gmt_cool
gmt_cool = np.array([[ 0.05,  0.95,  1.  ],
       [ 0.15,  0.85,  1.  ],
       [ 0.25,  0.75,  1.  ],
       [ 0.35,  0.65,  1.  ],
       [ 0.45,  0.55,  1.  ],
       [ 0.55,  0.45,  1.  ],
       [ 0.65,  0.35,  1.  ],
       [ 0.75,  0.25,  1.  ],
       [ 0.85,  0.15,  1.  ],
       [ 0.95,  0.05,  1.  ]])

# Diverging
# ---------

# 1. brown_blue
brown_blue = np.array([[ 0.2       ,  0.09803922,  0.        ],
       [ 0.4       ,  0.18431373,  0.        ],
       [ 0.6       ,  0.37647059,  0.20784314],
       [ 0.8       ,  0.60784314,  0.47843137],
       [ 0.84705882,  0.68627451,  0.59215686],
       [ 0.94901961,  0.85490196,  0.80392157],
       [ 0.8       ,  0.99215686,  1.        ],
       [ 0.6       ,  0.97254902,  1.        ],
       [ 0.39607843,  0.9372549 ,  1.        ],
       [ 0.19607843,  0.89019608,  1.        ],
       [ 0.        ,  0.6627451 ,  0.8       ],
       [ 0.        ,  0.47843137,  0.6       ]])

# 2. green_magenta
green_magenta = np.array([[ 0.        ,  0.31372549,  0.        ],
       [ 0.        ,  0.5254902 ,  0.        ],
       [ 0.        ,  0.73333333,  0.        ],
       [ 0.        ,  0.94509804,  0.        ],
       [ 0.31372549,  1.        ,  0.31372549],
       [ 0.5254902 ,  1.        ,  0.5254902 ],
       [ 0.73333333,  1.        ,  0.73333333],
       [ 1.        ,  1.        ,  1.        ],
       [ 1.        ,  0.94509804,  1.        ],
       [ 1.        ,  0.73333333,  1.        ],
       [ 1.        ,  0.5254902 ,  1.        ],
       [ 1.        ,  0.31372549,  1.        ],
       [ 0.94509804,  0.        ,  0.94509804],
       [ 0.73333333,  0.        ,  0.73333333],
       [ 0.5254902 ,  0.        ,  0.5254902 ],
       [ 0.31372549,  0.        ,  0.31372549]])

# 3. cmp_flux
cmp_flux = np.array([[ 0.        ,  0.99215686,  0.99215686],
       [ 0.03137255,  0.87058824,  0.99215686],
       [ 0.0627451 ,  0.74117647,  0.99215686],
       [ 0.09411765,  0.61568627,  0.99215686],
       [ 0.1254902 ,  0.49019608,  0.99215686],
       [ 0.15686275,  0.36470588,  0.99215686],
       [ 0.18823529,  0.23529412,  0.99215686],
       [ 0.33333333,  0.33333333,  0.99215686],
       [ 0.52156863,  0.52156863,  0.99215686],
       [ 0.70980392,  0.70980392,  0.99215686],
       [ 0.90196078,  0.90196078,  0.99215686],
       [ 0.99215686,  0.90196078,  0.90196078],
       [ 0.99215686,  0.70980392,  0.70980392],
       [ 0.99215686,  0.52156863,  0.52156863],
       [ 0.99215686,  0.33333333,  0.33333333],
       [ 0.99215686,  0.23529412,  0.18823529],
       [ 0.99215686,  0.36470588,  0.15686275],
       [ 0.99215686,  0.49019608,  0.1254902 ],
       [ 0.99215686,  0.61568627,  0.09411765],
       [ 0.99215686,  0.74117647,  0.0627451 ],
       [ 0.99215686,  0.87843137,  0.03137255],
       [ 0.99215686,  0.99215686,  0.        ]])


# Rainbow
# ------

# 1. AMWG
amwg = np.array([[ 0.57254902,  0.43921569,  0.85882353],
       [ 0.55294118,  0.41568627,  0.85490196],
       [ 0.52941176,  0.39607843,  0.85098039],
       [ 0.50588235,  0.37254902,  0.84705882],
       [ 0.48235294,  0.35294118,  0.84313725],
       [ 0.45882353,  0.32941176,  0.83921569],
       [ 0.43529412,  0.30980392,  0.83529412],
       [ 0.41176471,  0.29019608,  0.83137255],
       [ 0.38431373,  0.27058824,  0.83137255],
       [ 0.36078431,  0.24705882,  0.82745098],
       [ 0.33333333,  0.22745098,  0.82352941],
       [ 0.30980392,  0.20784314,  0.81960784],
       [ 0.28235294,  0.18823529,  0.81568627],
       [ 0.25490196,  0.16862745,  0.81176471],
       [ 0.22745098,  0.14901961,  0.80784314],
       [ 0.2       ,  0.12941176,  0.80784314],
       [ 0.17254902,  0.10980392,  0.80392157],
       [ 0.14509804,  0.09019608,  0.8       ],
       [ 0.11372549,  0.07058824,  0.79607843],
       [ 0.08627451,  0.05490196,  0.79215686],
       [ 0.05882353,  0.03529412,  0.78823529],
       [ 0.02745098,  0.01568627,  0.78431373],
       [ 0.        ,  0.        ,  0.78431373],
       [ 0.00784314,  0.01568627,  0.78823529],
       [ 0.01568627,  0.03529412,  0.79215686],
       [ 0.02745098,  0.05098039,  0.8       ],
       [ 0.03529412,  0.07058824,  0.80392157],
       [ 0.04705882,  0.08627451,  0.80784314],
       [ 0.05490196,  0.10588235,  0.81568627],
       [ 0.06666667,  0.12156863,  0.81960784],
       [ 0.07843137,  0.14117647,  0.82352941],
       [ 0.08627451,  0.15686275,  0.83137255],
       [ 0.09803922,  0.17647059,  0.83529412],
       [ 0.10980392,  0.19607843,  0.84313725],
       [ 0.11764706,  0.21176471,  0.84705882],
       [ 0.12941176,  0.23137255,  0.85098039],
       [ 0.14117647,  0.24705882,  0.85882353],
       [ 0.15294118,  0.26666667,  0.8627451 ],
       [ 0.16470588,  0.28235294,  0.86666667],
       [ 0.17254902,  0.30196078,  0.8745098 ],
       [ 0.18431373,  0.31764706,  0.87843137],
       [ 0.19607843,  0.3372549 ,  0.88235294],
       [ 0.20784314,  0.35294118,  0.89019608],
       [ 0.21960784,  0.37254902,  0.89411765],
       [ 0.23529412,  0.38823529,  0.90196078],
       [ 0.24313725,  0.4       ,  0.90196078],
       [ 0.25490196,  0.41176471,  0.90588235],
       [ 0.2627451 ,  0.41960784,  0.90588235],
       [ 0.2745098 ,  0.43137255,  0.90980392],
       [ 0.28627451,  0.43921569,  0.90980392],
       [ 0.29411765,  0.45098039,  0.91372549],
       [ 0.30588235,  0.45882353,  0.91372549],
       [ 0.31764706,  0.47058824,  0.91764706],
       [ 0.3254902 ,  0.47843137,  0.91764706],
       [ 0.3372549 ,  0.49019608,  0.92156863],
       [ 0.34901961,  0.49803922,  0.9254902 ],
       [ 0.36078431,  0.50980392,  0.9254902 ],
       [ 0.36862745,  0.51764706,  0.92941176],
       [ 0.38039216,  0.52941176,  0.92941176],
       [ 0.39215686,  0.5372549 ,  0.93333333],
       [ 0.40392157,  0.54901961,  0.93333333],
       [ 0.41176471,  0.55686275,  0.9372549 ],
       [ 0.42352941,  0.56862745,  0.9372549 ],
       [ 0.43529412,  0.57647059,  0.94117647],
       [ 0.44705882,  0.58823529,  0.94117647],
       [ 0.45882353,  0.59607843,  0.94509804],
       [ 0.47058824,  0.60784314,  0.94901961],
       [ 0.47843137,  0.62745098,  0.94509804],
       [ 0.49019608,  0.64313725,  0.94117647],
       [ 0.50196078,  0.6627451 ,  0.94117647],
       [ 0.50980392,  0.67843137,  0.9372549 ],
       [ 0.52156863,  0.69803922,  0.9372549 ],
       [ 0.52941176,  0.71372549,  0.93333333],
       [ 0.54117647,  0.72941176,  0.93333333],
       [ 0.55294118,  0.74117647,  0.92941176],
       [ 0.56078431,  0.75686275,  0.92941176],
       [ 0.57254902,  0.76862745,  0.9254902 ],
       [ 0.58039216,  0.78431373,  0.9254902 ],
       [ 0.59215686,  0.79607843,  0.92156863],
       [ 0.6       ,  0.80392157,  0.91764706],
       [ 0.61176471,  0.81568627,  0.91764706],
       [ 0.61960784,  0.82745098,  0.91372549],
       [ 0.63137255,  0.83529412,  0.91372549],
       [ 0.63921569,  0.84313725,  0.90980392],
       [ 0.65098039,  0.85098039,  0.90980392],
       [ 0.65882353,  0.85882353,  0.90588235],
       [ 0.67058824,  0.86666667,  0.90588235],
       [ 0.67843137,  0.87058824,  0.90196078],
       [ 0.69019608,  0.87843137,  0.90196078],
       [ 0.68627451,  0.87843137,  0.90588235],
       [ 0.68235294,  0.88235294,  0.90980392],
       [ 0.67843137,  0.88627451,  0.91372549],
       [ 0.6745098 ,  0.89019608,  0.91764706],
       [ 0.67058824,  0.89411765,  0.92156863],
       [ 0.66666667,  0.89803922,  0.92941176],
       [ 0.65882353,  0.90196078,  0.93333333],
       [ 0.65490196,  0.90588235,  0.9372549 ],
       [ 0.65098039,  0.90980392,  0.94117647],
       [ 0.64705882,  0.91372549,  0.94509804],
       [ 0.64313725,  0.91764706,  0.95294118],
       [ 0.63921569,  0.92156863,  0.95686275],
       [ 0.63529412,  0.9254902 ,  0.96078431],
       [ 0.62745098,  0.92941176,  0.96470588],
       [ 0.62352941,  0.93333333,  0.96862745],
       [ 0.61960784,  0.9372549 ,  0.97647059],
       [ 0.61568627,  0.94117647,  0.98039216],
       [ 0.60784314,  0.94509804,  0.98431373],
       [ 0.60392157,  0.94901961,  0.98823529],
       [ 0.6       ,  0.95294118,  0.99215686],
       [ 0.59607843,  0.96078431,  1.        ],
       [ 0.59607843,  0.97254902,  0.98823529],
       [ 0.6       ,  0.97647059,  0.96470588],
       [ 0.6       ,  0.96470588,  0.92941176],
       [ 0.60392157,  0.95294118,  0.89411765],
       [ 0.60392157,  0.94117647,  0.8627451 ],
       [ 0.60392157,  0.92941176,  0.83529412],
       [ 0.60784314,  0.91764706,  0.80784314],
       [ 0.60784314,  0.90588235,  0.78039216],
       [ 0.60784314,  0.89411765,  0.75686275],
       [ 0.60784314,  0.88235294,  0.73333333],
       [ 0.60784314,  0.87058824,  0.70980392],
       [ 0.60784314,  0.85882353,  0.69019608],
       [ 0.60784314,  0.84705882,  0.67058824],
       [ 0.60784314,  0.83529412,  0.65098039],
       [ 0.60784314,  0.82352941,  0.63529412],
       [ 0.60784314,  0.81176471,  0.61960784],
       [ 0.60784314,  0.80392157,  0.60784314],
       [ 0.96078431,  0.90196078,  0.74509804],
       [ 0.95294118,  0.89019608,  0.72941176],
       [ 0.94901961,  0.88235294,  0.71764706],
       [ 0.94117647,  0.87058824,  0.70196078],
       [ 0.9372549 ,  0.85882353,  0.69019608],
       [ 0.93333333,  0.85098039,  0.67843137],
       [ 0.9254902 ,  0.83921569,  0.6627451 ],
       [ 0.92156863,  0.83137255,  0.65098039],
       [ 0.91764706,  0.81960784,  0.63921569],
       [ 0.90980392,  0.80784314,  0.62352941],
       [ 0.90588235,  0.79607843,  0.61176471],
       [ 0.90196078,  0.78823529,  0.6       ],
       [ 0.89411765,  0.77647059,  0.58823529],
       [ 0.89019608,  0.76470588,  0.57647059],
       [ 0.88627451,  0.75294118,  0.56470588],
       [ 0.87843137,  0.74117647,  0.55294118],
       [ 0.8745098 ,  0.72941176,  0.54117647],
       [ 0.87058824,  0.72156863,  0.52941176],
       [ 0.8745098 ,  0.71764706,  0.50588235],
       [ 0.88235294,  0.71764706,  0.48235294],
       [ 0.88627451,  0.72156863,  0.4627451 ],
       [ 0.89411765,  0.72156863,  0.43921569],
       [ 0.89803922,  0.7254902 ,  0.41568627],
       [ 0.90588235,  0.72941176,  0.39215686],
       [ 0.91372549,  0.73333333,  0.36862745],
       [ 0.91764706,  0.7372549 ,  0.34509804],
       [ 0.9254902 ,  0.74117647,  0.32156863],
       [ 0.92941176,  0.74901961,  0.29411765],
       [ 0.9372549 ,  0.75686275,  0.27058824],
       [ 0.94117647,  0.76470588,  0.24313725],
       [ 0.94901961,  0.77254902,  0.21960784],
       [ 0.95686275,  0.78431373,  0.19215686],
       [ 0.96078431,  0.79607843,  0.16470588],
       [ 0.96862745,  0.80784314,  0.1372549 ],
       [ 0.97254902,  0.81960784,  0.10980392],
       [ 0.98039216,  0.83137255,  0.08235294],
       [ 0.98431373,  0.84705882,  0.05490196],
       [ 0.99215686,  0.8627451 ,  0.02745098],
       [ 1.        ,  0.88235294,  0.        ],
       [ 1.        ,  0.87058824,  0.        ],
       [ 1.        ,  0.85882353,  0.        ],
       [ 1.        ,  0.84705882,  0.        ],
       [ 1.        ,  0.83921569,  0.        ],
       [ 1.        ,  0.82745098,  0.        ],
       [ 1.        ,  0.81568627,  0.        ],
       [ 1.        ,  0.80392157,  0.        ],
       [ 1.        ,  0.79607843,  0.        ],
       [ 1.        ,  0.78431373,  0.        ],
       [ 1.        ,  0.77254902,  0.        ],
       [ 1.        ,  0.76470588,  0.        ],
       [ 1.        ,  0.75294118,  0.        ],
       [ 1.        ,  0.74117647,  0.        ],
       [ 1.        ,  0.72941176,  0.        ],
       [ 1.        ,  0.72156863,  0.        ],
       [ 1.        ,  0.70980392,  0.        ],
       [ 1.        ,  0.69803922,  0.        ],
       [ 1.        ,  0.68627451,  0.        ],
       [ 1.        ,  0.67843137,  0.        ],
       [ 1.        ,  0.66666667,  0.        ],
       [ 1.        ,  0.65490196,  0.        ],
       [ 1.        ,  0.64705882,  0.        ],
       [ 1.        ,  0.62745098,  0.        ],
       [ 1.        ,  0.61176471,  0.        ],
       [ 1.        ,  0.59215686,  0.        ],
       [ 1.        ,  0.57647059,  0.        ],
       [ 1.        ,  0.56078431,  0.        ],
       [ 1.        ,  0.54117647,  0.        ],
       [ 1.        ,  0.5254902 ,  0.        ],
       [ 1.        ,  0.50980392,  0.        ],
       [ 1.        ,  0.49019608,  0.        ],
       [ 1.        ,  0.4745098 ,  0.        ],
       [ 1.        ,  0.45882353,  0.        ],
       [ 1.        ,  0.43921569,  0.        ],
       [ 1.        ,  0.42352941,  0.        ],
       [ 1.        ,  0.40392157,  0.        ],
       [ 1.        ,  0.38823529,  0.        ],
       [ 1.        ,  0.37254902,  0.        ],
       [ 1.        ,  0.35294118,  0.        ],
       [ 1.        ,  0.3372549 ,  0.        ],
       [ 1.        ,  0.32156863,  0.        ],
       [ 1.        ,  0.30196078,  0.        ],
       [ 1.        ,  0.28627451,  0.        ],
       [ 1.        ,  0.27058824,  0.        ],
       [ 0.98431373,  0.25882353,  0.00784314],
       [ 0.97254902,  0.25098039,  0.01568627],
       [ 0.95686275,  0.24313725,  0.02352941],
       [ 0.94509804,  0.23137255,  0.03137255],
       [ 0.92941176,  0.22352941,  0.03921569],
       [ 0.91764706,  0.21568627,  0.04705882],
       [ 0.90196078,  0.20784314,  0.05490196],
       [ 0.89019608,  0.20392157,  0.05882353],
       [ 0.8745098 ,  0.19607843,  0.06666667],
       [ 0.8627451 ,  0.18823529,  0.0745098 ],
       [ 0.84705882,  0.18431373,  0.07843137],
       [ 0.83529412,  0.17647059,  0.08627451],
       [ 0.81960784,  0.17254902,  0.09019608],
       [ 0.80784314,  0.16470588,  0.09803922],
       [ 0.79215686,  0.16078431,  0.10196078],
       [ 0.78039216,  0.15686275,  0.10588235],
       [ 0.76470588,  0.15294118,  0.10980392],
       [ 0.75294118,  0.14509804,  0.11764706],
       [ 0.7372549 ,  0.14117647,  0.12156863],
       [ 0.7254902 ,  0.1372549 ,  0.1254902 ],
       [ 0.70980392,  0.13333333,  0.12941176],
       [ 0.69803922,  0.13333333,  0.13333333],
       [ 0.70980392,  0.14901961,  0.14901961],
       [ 0.7254902 ,  0.16862745,  0.16862745],
       [ 0.7372549 ,  0.19215686,  0.19215686],
       [ 0.75294118,  0.21176471,  0.21176471],
       [ 0.76470588,  0.23137255,  0.23137255],
       [ 0.78039216,  0.25490196,  0.25490196],
       [ 0.79215686,  0.27843137,  0.27843137],
       [ 0.80784314,  0.30196078,  0.30196078],
       [ 0.81960784,  0.3254902 ,  0.3254902 ],
       [ 0.83529412,  0.34901961,  0.34901961],
       [ 0.84705882,  0.37647059,  0.37647059],
       [ 0.8627451 ,  0.4       ,  0.4       ],
       [ 0.8745098 ,  0.42745098,  0.42745098],
       [ 0.89019608,  0.45490196,  0.45490196],
       [ 0.90196078,  0.48235294,  0.48235294],
       [ 0.91764706,  0.50980392,  0.50980392],
       [ 0.92941176,  0.54117647,  0.54117647],
       [ 0.94509804,  0.57254902,  0.57254902],
       [ 0.95686275,  0.6       ,  0.6       ],
       [ 0.97254902,  0.63137255,  0.63137255],
       [ 0.98431373,  0.6627451 ,  0.6627451 ],
       [ 1.        ,  0.69803922,  0.69803922]])

# 2. nice_gfdl
nice_gfdl = np.array([[ 0.996078,  0.984314,  0.964706],
       [ 0.92549 ,  0.929412,  0.945098],
       [ 0.905882,  0.909804,  0.92549 ],
       [ 0.862745,  0.882353,  0.901961],
       [ 0.835294,  0.854902,  0.87451 ],
       [ 0.811765,  0.823529,  0.858824],
       [ 0.784314,  0.796078,  0.831373],
       [ 0.74902 ,  0.772549,  0.811765],
       [ 0.729412,  0.74902 ,  0.788235],
       [ 0.694118,  0.717647,  0.768627],
       [ 0.670588,  0.690196,  0.741176],
       [ 0.639216,  0.666667,  0.72549 ],
       [ 0.611765,  0.639216,  0.698039],
       [ 0.580392,  0.607843,  0.666667],
       [ 0.560784,  0.588235,  0.647059],
       [ 0.517647,  0.560784,  0.623529],
       [ 0.490196,  0.537255,  0.596078],
       [ 0.462745,  0.517647,  0.576471],
       [ 0.435294,  0.490196,  0.545098],
       [ 0.4     ,  0.447059,  0.52549 ],
       [ 0.384314,  0.431373,  0.509804],
       [ 0.352941,  0.407843,  0.486275],
       [ 0.32549 ,  0.380392,  0.458824],
       [ 0.294118,  0.356863,  0.443137],
       [ 0.270588,  0.329412,  0.415686],
       [ 0.247059,  0.301961,  0.396078],
       [ 0.223529,  0.282353,  0.372549],
       [ 0.196078,  0.254902,  0.360784],
       [ 0.168627,  0.223529,  0.32549 ],
       [ 0.133333,  0.203922,  0.301961],
       [ 0.113725,  0.180392,  0.27451 ],
       [ 0.094118,  0.14902 ,  0.25098 ],
       [ 0.07451 ,  0.12549 ,  0.227451],
       [ 0.05098 ,  0.109804,  0.203922],
       [ 0.047059,  0.105882,  0.196078],
       [ 0.05098 ,  0.117647,  0.203922],
       [ 0.062745,  0.129412,  0.219608],
       [ 0.07451 ,  0.141176,  0.235294],
       [ 0.086275,  0.156863,  0.254902],
       [ 0.094118,  0.176471,  0.258824],
       [ 0.105882,  0.188235,  0.27451 ],
       [ 0.121569,  0.207843,  0.298039],
       [ 0.133333,  0.219608,  0.309804],
       [ 0.137255,  0.243137,  0.32549 ],
       [ 0.145098,  0.254902,  0.337255],
       [ 0.160784,  0.270588,  0.356863],
       [ 0.176471,  0.286275,  0.372549],
       [ 0.180392,  0.301961,  0.380392],
       [ 0.196078,  0.313725,  0.396078],
       [ 0.203922,  0.32549 ,  0.407843],
       [ 0.219608,  0.341176,  0.423529],
       [ 0.223529,  0.360784,  0.427451],
       [ 0.247059,  0.384314,  0.45098 ],
       [ 0.247059,  0.396078,  0.458824],
       [ 0.262745,  0.415686,  0.478431],
       [ 0.282353,  0.439216,  0.490196],
       [ 0.290196,  0.447059,  0.498039],
       [ 0.298039,  0.462745,  0.513725],
       [ 0.309804,  0.478431,  0.529412],
       [ 0.313725,  0.501961,  0.533333],
       [ 0.329412,  0.517647,  0.54902 ],
       [ 0.333333,  0.529412,  0.560784],
       [ 0.34902 ,  0.54902 ,  0.580392],
       [ 0.356863,  0.564706,  0.592157],
       [ 0.372549,  0.580392,  0.607843],
       [ 0.392157,  0.603922,  0.631373],
       [ 0.403922,  0.615686,  0.643137],
       [ 0.403922,  0.631373,  0.643137],
       [ 0.423529,  0.654902,  0.666667],
       [ 0.431373,  0.662745,  0.67451 ],
       [ 0.447059,  0.678431,  0.694118],
       [ 0.454902,  0.698039,  0.705882],
       [ 0.47451 ,  0.717647,  0.72549 ],
       [ 0.482353,  0.72549 ,  0.733333],
       [ 0.501961,  0.74902 ,  0.756863],
       [ 0.505882,  0.772549,  0.752941],
       [ 0.517647,  0.788235,  0.764706],
       [ 0.52549 ,  0.807843,  0.784314],
       [ 0.541176,  0.819608,  0.8     ],
       [ 0.54902 ,  0.839216,  0.811765],
       [ 0.564706,  0.858824,  0.831373],
       [ 0.580392,  0.87451 ,  0.847059],
       [ 0.596078,  0.894118,  0.862745],
       [ 0.596078,  0.905882,  0.862745],
       [ 0.596078,  0.905882,  0.862745],
       [ 0.576471,  0.890196,  0.819608],
       [ 0.564706,  0.878431,  0.811765],
       [ 0.54902 ,  0.866667,  0.760784],
       [ 0.541176,  0.858824,  0.752941],
       [ 0.529412,  0.847059,  0.729412],
       [ 0.517647,  0.835294,  0.713725],
       [ 0.498039,  0.827451,  0.662745],
       [ 0.478431,  0.807843,  0.643137],
       [ 0.470588,  0.803922,  0.607843],
       [ 0.454902,  0.784314,  0.588235],
       [ 0.443137,  0.776471,  0.556863],
       [ 0.431373,  0.764706,  0.545098],
       [ 0.415686,  0.74902 ,  0.501961],
       [ 0.407843,  0.741176,  0.494118],
       [ 0.392157,  0.729412,  0.458824],
       [ 0.380392,  0.713725,  0.447059],
       [ 0.368627,  0.701961,  0.415686],
       [ 0.352941,  0.682353,  0.4     ],
       [ 0.345098,  0.678431,  0.360784],
       [ 0.329412,  0.662745,  0.345098],
       [ 0.317647,  0.647059,  0.32549 ],
       [ 0.305882,  0.635294,  0.313725],
       [ 0.282353,  0.623529,  0.270588],
       [ 0.27451 ,  0.615686,  0.262745],
       [ 0.262745,  0.592157,  0.223529],
       [ 0.258824,  0.584314,  0.215686],
       [ 0.247059,  0.576471,  0.180392],
       [ 0.243137,  0.572549,  0.176471],
       [ 0.270588,  0.584314,  0.14902 ],
       [ 0.282353,  0.6     ,  0.160784],
       [ 0.313725,  0.619608,  0.117647],
       [ 0.329412,  0.639216,  0.129412],
       [ 0.372549,  0.654902,  0.098039],
       [ 0.384314,  0.666667,  0.109804],
       [ 0.419608,  0.686275,  0.070588],
       [ 0.435294,  0.701961,  0.086275],
       [ 0.478431,  0.721569,  0.023529],
       [ 0.494118,  0.741176,  0.05098 ],
       [ 0.529412,  0.756863,  0.      ],
       [ 0.545098,  0.772549,  0.      ],
       [ 0.588235,  0.788235,  0.      ],
       [ 0.603922,  0.807843,  0.      ],
       [ 0.635294,  0.811765,  0.      ],
       [ 0.658824,  0.835294,  0.      ],
       [ 0.698039,  0.85098 ,  0.      ],
       [ 0.721569,  0.87451 ,  0.      ],
       [ 0.756863,  0.878431,  0.      ],
       [ 0.780392,  0.905882,  0.      ],
       [ 0.823529,  0.909804,  0.      ],
       [ 0.847059,  0.933333,  0.      ],
       [ 0.878431,  0.945098,  0.      ],
       [ 0.901961,  0.968627,  0.      ],
       [ 0.933333,  0.972549,  0.      ],
       [ 0.960784,  1.      ,  0.      ],
       [ 1.      ,  1.      ,  0.      ],
       [ 1.      ,  1.      ,  0.      ],
       [ 1.      ,  0.984314,  0.      ],
       [ 1.      ,  0.972549,  0.      ],
       [ 1.      ,  0.921569,  0.      ],
       [ 1.      ,  0.905882,  0.      ],
       [ 1.      ,  0.862745,  0.      ],
       [ 1.      ,  0.847059,  0.      ],
       [ 1.      ,  0.803922,  0.      ],
       [ 1.      ,  0.788235,  0.      ],
       [ 1.      ,  0.74902 ,  0.      ],
       [ 1.      ,  0.733333,  0.      ],
       [ 1.      ,  0.694118,  0.      ],
       [ 1.      ,  0.678431,  0.      ],
       [ 1.      ,  0.631373,  0.      ],
       [ 1.      ,  0.619608,  0.      ],
       [ 1.      ,  0.580392,  0.      ],
       [ 1.      ,  0.568627,  0.      ],
       [ 1.      ,  0.529412,  0.      ],
       [ 1.      ,  0.509804,  0.      ],
       [ 1.      ,  0.466667,  0.      ],
       [ 1.      ,  0.458824,  0.      ],
       [ 1.      ,  0.431373,  0.      ],
       [ 1.      ,  0.407843,  0.      ],
       [ 1.      ,  0.376471,  0.      ],
       [ 0.980392,  0.360784,  0.      ],
       [ 0.952941,  0.333333,  0.      ],
       [ 0.929412,  0.313725,  0.      ],
       [ 0.909804,  0.290196,  0.      ],
       [ 0.886275,  0.270588,  0.      ],
       [ 0.862745,  0.243137,  0.      ],
       [ 0.843137,  0.231373,  0.      ],
       [ 0.819608,  0.203922,  0.      ],
       [ 0.792157,  0.184314,  0.      ],
       [ 0.772549,  0.160784,  0.      ],
       [ 0.74902 ,  0.145098,  0.      ],
       [ 0.72549 ,  0.121569,  0.023529],
       [ 0.721569,  0.117647,  0.019608],
       [ 0.686275,  0.12549 ,  0.023529],
       [ 0.67451 ,  0.117647,  0.011765],
       [ 0.631373,  0.117647,  0.035294],
       [ 0.627451,  0.117647,  0.031373],
       [ 0.603922,  0.109804,  0.031373],
       [ 0.592157,  0.101961,  0.023529],
       [ 0.54902 ,  0.105882,  0.035294],
       [ 0.545098,  0.101961,  0.031373],
       [ 0.505882,  0.101961,  0.027451],
       [ 0.501961,  0.098039,  0.023529],
       [ 0.47451 ,  0.101961,  0.035294],
       [ 0.466667,  0.098039,  0.031373],
       [ 0.431373,  0.094118,  0.039216],
       [ 0.427451,  0.090196,  0.035294],
       [ 0.392157,  0.094118,  0.039216],
       [ 0.388235,  0.090196,  0.035294],
       [ 0.360784,  0.086275,  0.039216],
       [ 0.34902 ,  0.078431,  0.031373],
       [ 0.313725,  0.086275,  0.047059],
       [ 0.301961,  0.078431,  0.043137],
       [ 0.290196,  0.078431,  0.043137],
       [ 0.278431,  0.070588,  0.039216],
       [ 0.239216,  0.07451 ,  0.039216],
       [ 0.235294,  0.070588,  0.039216],
       [ 0.215686,  0.066667,  0.043137],
       [ 0.207843,  0.062745,  0.039216],
       [ 0.180392,  0.062745,  0.043137],
       [ 0.160784,  0.05098 ,  0.031373],
       [ 0.141176,  0.054902,  0.035294],
       [ 0.137255,  0.05098 ,  0.031373],
       [ 0.113725,  0.05098 ,  0.035294],
       [ 0.101961,  0.043137,  0.023529],
       [ 0.082353,  0.043137,  0.031373],
       [ 0.070588,  0.031373,  0.019608],
       [ 0.058824,  0.031373,  0.023529],
       [ 0.058824,  0.031373,  0.023529],
       [ 0.054902,  0.031373,  0.019608],
       [ 0.05098 ,  0.031373,  0.015686],
       [ 0.047059,  0.023529,  0.019608],
       [ 0.05098 ,  0.027451,  0.023529],
       [ 0.043137,  0.027451,  0.019608],
       [ 0.039216,  0.015686,  0.      ],
       [ 0.035294,  0.019608,  0.015686],
       [ 0.031373,  0.011765,  0.      ],
       [ 0.023529,  0.015686,  0.      ],
       [ 0.023529,  0.015686,  0.      ],
       [ 0.      ,  0.      ,  0.      ],
       [ 0.      ,  0.      ,  0.      ]])
