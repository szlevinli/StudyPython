# -*- coding: utf8 -*-
def isOverWeight(grossWeights=1, pieces=1, threshold=80):
    '''判断是否超重 true=是 false=否
    grossWeights=毛重 KG
    pieces=件数
    threshold=阈值 KG
    '''
    average = grossWeights / pieces
    return average > threshold


def isOverLong(longs=0, widths=0, highs=0,
               singleThreshold=160, perimeterThreshold=300):
    '''判断是否超长 true=是 false=否
    longs=长 cm, widths=宽 cm, highs=高 cm
    singleThreshold=单边长度阈值 cm
    perimeterThreshold=周长阈值 cm
    '''
    perimeter = longs + widths + highs
    return longs > singleThreshold or widths > singleThreshold \
        or highs > singleThreshold or perimeter > perimeterThreshold


def _getRate(prodCode, regionType):
    '''获取抛重比
    '''
    return 9000


def _getPrice(prodCode):
    '''获取产品定价
    prodCode=产品编码
    '''
    return 1


def _getOfferPrice(prodCode):
    '''获取产品报价
    prodCode=产品编码
    '''
    return 1


def _getMiniChargedPrice(prodCode):
    '''获取产品定价的最低收费
    prodCode=产品编码
    '''
    return 20


def _getMiniChargedOfferPrice(prodCode):
    '''获取产品报价的最低收费
    prodCode=产品编码
    '''
    return 20


def calculateChargedWeight(longs=0, widths=0, highs=0,
                           rate=6000, grossWeight=0):
    '''计算计费重量
    @param longs->float unit:cm
    @param widths->float unit:cm
    @param highs->float unit:cm
    @param rate->int 轻抛比 (6000/9000/12000)
    @param grossWeight->float 毛重
    '''
    chargeWeight = (longs * widths * highs) / rate
    return chargeWeight if chargeWeight > grossWeight else grossWeight


def calculateOverLongChargedWeight(longs=0, widths=0, highs=0,
                                   rate=6000, grossWeight=0):
    '''计算超长计费重量
    longs=长 cm, widths=宽 cm, highs=高 cm
    rate=轻抛比, grossWeight=毛重
    '''
    return calculateChargedWeight(longs, widths, highs, rate, grossWeight)


def calculateOverWeightPrice(chargedWeight, unitPrice, miniChargedPrice):
    '''计算超重价格
    chargedWeight=计费重量
    unitPrice=单价 元/KG
    miniChargedPrice=最低收费
    '''
    price = chargedWeight * unitPrice
    return price if price > miniChargedPrice else miniChargedPrice


def calculateOverLongPrice(overLongChargedWeight,
                           unitPrice, miniChargedPrice):
    '''计算超长价格
    overLongChargedWeight=超长计费重量
    unitPrice=单价 元/KG
    miniChargedPrice=最低收费
    '''
    return calculateOverWeightPrice(overLongChargedWeight,
                                    unitPrice, miniChargedPrice)
if __name__ == '__main__':
    overWeightPrice = 0
    overLongPrice = 0

    longs = 79
    widths = 81
    highs = 150
    productCode = 'VA0006'
    regionType = 'R20101'  # 区域类型
    grossWeights = 89.61
    pieces = 1

    # 单价
    unitPrice = _getOfferPrice(productCode)
    # 最低收费
    miniChargedPrice = _getMiniChargedOfferPrice(productCode)
    # 轻抛比
    rate = _getRate(productCode, regionType)
    # 计费重量
    chargedWeight = calculateChargedWeight(
        longs, widths, highs, rate, grossWeights)
    # 超长计费重量
    overLongChargedWeight = calculateOverLongChargedWeight(
        longs, widths, highs, rate, grossWeights)

    if isOverWeight(grossWeights, pieces, threshold=80):
        overWeightPrice = calculateOverWeightPrice(
            chargedWeight, unitPrice, miniChargedPrice)
    else:
        overLongPrice = calculateOverLongPrice(
            overLongChargedWeight, unitPrice, miniChargedPrice)

    print("overWeightPrice = ", overWeightPrice)
    print("overLongPrice = ", overLongPrice)
