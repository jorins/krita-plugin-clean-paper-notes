from krita import *


def pencil():
    return [
        pencilLightnessFilter(),
        pencilColorToAlphaFilter(),
        pencilAlphaFilter()
    ]


def ink():
    return [
        inkLightnessFilter(),
        inkColorToAlphaFilter(),
        inkAlphaFilter()
    ]


def pencilLightnessFilter():
    lightnessFilter = Krita.instance().filter('levels')
    lightnessConfig = lightnessFilter.configuration()
    lightnessConfig.setProperty('mode', 'channels')
    lightnessConfig.setProperty('histogram_mode', 'logarithmic')
    lightnessConfig.setProperty('number_of_channels', 8)
    lightnessConfig.setProperty('channel_0', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_1', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_2', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_3', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_4', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_5', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_6', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_7', '0.5;0.9;1;0;1')
    lightnessConfig.setProperty('lightness', '0.540;0.912;0.9;0;1')
    lightnessConfig.setProperty('blackvalue', 138)
    lightnessConfig.setProperty('whitevalue', 233)
    lightnessConfig.setProperty('gammavalue', 0.9)
    lightnessConfig.setProperty('outblackvalue', 0)
    lightnessConfig.setProperty('outwhitevalue', 255)

    return lightnessFilter


def pencilColorToAlphaFilter():
    ctoaFilter = Krita.instance().filter('colortoalpha')
    ctoaConfig = ctoaFilter.configuration()
    ctoaConfig.setProperty('targetcolor', '#ffffff')
    ctoaConfig.setProperty('threshold', 90)

    return ctoaFilter


def pencilAlphaFilter():
    alphaFilter = Krita.instance().filter('levels')
    alphaConfig = alphaFilter.configuration()
    alphaConfig.setProperty('mode', 'channels')
    alphaConfig.setProperty('histogram_mode', 'logarithmic')
    alphaConfig.setProperty('number_of_channels', 8)
    alphaConfig.setProperty('channel_0', '0;1;1;0;1')
    alphaConfig.setProperty('channel_1', '0;1;1;0;1')
    alphaConfig.setProperty('channel_2', '0;1;1;0;1')
    alphaConfig.setProperty('channel_3', '0;1;1;0;1')
    alphaConfig.setProperty('channel_4', '0.048;1;1.7;0;1')
    alphaConfig.setProperty('channel_5', '0;1;1;0;1')
    alphaConfig.setProperty('channel_6', '0;1;1;0;1')
    alphaConfig.setProperty('channel_7', '0;1;1;0;1')

    return alphaFilter


def inkLightnessFilter():
    lightnessFilter = Krita.instance().filter('levels')
    lightnessConfig = lightnessFilter.configuration()
    lightnessConfig.setProperty('mode', 'channels')
    lightnessConfig.setProperty('histogram_mode', 'logarithmic')
    lightnessConfig.setProperty('number_of_channels', 8)
    lightnessConfig.setProperty('channel_0', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_1', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_2', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_3', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_4', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_5', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_6', '0;1;1;0;1')
    lightnessConfig.setProperty('channel_7', '0.4;0.8;0.5;0;1')
    lightnessConfig.setProperty('lightness', '0.392;0.946;0.672;0;1')
    lightnessConfig.setProperty('blackvalue', 100)
    lightnessConfig.setProperty('whitevalue', 241)
    lightnessConfig.setProperty('gammavalue', 0.672)
    lightnessConfig.setProperty('outblackvalue', 0)
    lightnessConfig.setProperty('outwhitevalue', 255)

    return lightnessFilter


def inkColorToAlphaFilter():
    ctoaFilter = Krita.instance().filter('colortoalpha')
    ctoaConfig = ctoaFilter.configuration()
    ctoaConfig.setProperty('targetcolor', '#ffffff')
    ctoaConfig.setProperty('threshold', 110)

    return ctoaFilter


def inkAlphaFilter():
    alphaFilter = Krita.instance().filter('levels')
    alphaConfig = alphaFilter.configuration()
    alphaConfig.setProperty('mode', 'channels')
    alphaConfig.setProperty('histogram_mode', 'logarithmic')
    alphaConfig.setProperty('number_of_channels', 8)
    alphaConfig.setProperty('channel_0', '0;1;1.752;0;1')
    # RGBA 0, 1,752, 255
    alphaConfig.setProperty('channel_1', '0;1;1;0;1')
    alphaConfig.setProperty('channel_2', '0;1;1;0;1')
    alphaConfig.setProperty('channel_3', '0;1;1;0;1')
    alphaConfig.setProperty('channel_4', '0.040;1;1;0;1')
    # Alpha 10, 1,000, 255
    alphaConfig.setProperty('channel_5', '0;1;1;0;1')
    alphaConfig.setProperty('channel_6', '0;1;1;0;1')
    alphaConfig.setProperty('channel_7', '0;1;1;0;1')

    return alphaFilter
