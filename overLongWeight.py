# -*- coding: utf-8 -*-


def isOverWeight(grossWeights=1, pieces=1, overWeightThreshold=80):
    '''判断是否超重
    @param grossWeights->float 毛重 unit: kg
    @param pieces->int 件数
    @param overWeightThreshold->float 超重阈值 unit: kg
    @return->boolean true: 超重, false: 不超重
    '''
    assert pieces > 0, "件数必须大于0"
    assert grossWeights >= 0, "毛重必须大于等于0"
    average = grossWeights / pieces
    return average > overWeightThreshold


def isOverLong(longs=0, widths=0, highs=0,
               overLongSingleThreshold=160, overLongPerimeterThreshold=300):
    '''判断是否超长
    @param longs->float unit: cm
    @param widths->float unit: cm
    @param highs->float unit: cm
    @param overLongSingleThreshold->float 超长单边阈值 unit: cm
    @param overLongPerimeterThreshold->float 超长周长阈值 unit: cm
    @return->boolean true: 超长, false: 不超长
    '''
    perimeter = longs + widths + highs
    return longs > overLongSingleThreshold or \
        widths > overLongSingleThreshold or \
        highs > overLongSingleThreshold or \
        perimeter > overLongPerimeterThreshold


def _getRate(prodCode, regionType):
    '''获取抛重比
    @param prodCode->str 产品编码
    @param regionType->str 区域类型编码 R20101(省内件)/...
    @return->float 轻抛比 6000/9000/12000
    '''
    return 9000


def _getPrice(prodCode):
    '''获取产品定价
    @param prodCode->str 产品编码
    @return->float
    '''
    return 1


def _getOfferPrice(prodCode):
    '''获取产品报价
    @param prodCode->float 产品编码
    @return->float
    '''
    return 1


def _getMiniChargedPrice(prodCode):
    '''获取产品定价的最低收费
    @param prodCode->str 产品编码
    @return->float
    '''
    return 20


def _getMiniChargedOfferPrice(prodCode):
    '''获取产品报价的最低收费
    @param prodCode->str 产品编码
    @return->float
    '''
    return 20


def _getOverWeightThreshold():
    '''获取超重阈值
    @return->float unit: kg
    '''
    return 80


def _getOverLongSingleThreshold():
    '''获取超长单边阈值
    @return->float unit: cm
    '''
    return 160


def _getOverLongPerimeterThreshold():
    '''获取超长周长阈值
    @return->float unit: cm
    '''
    return 300


def calculateChargedWeight(longs=0, widths=0, highs=0,
                           rate=6000, grossWeights=0):
    '''计算计费重量
    @param longs->float unit:cm
    @param widths->float unit:cm
    @param highs->float unit:cm
    @param rate->int 轻抛比 (6000/9000/12000)
    @param grossWeights->float 毛重
    @return->float
    '''
    chargeWeight = (longs * widths * highs) / rate
    return chargeWeight if chargeWeight > grossWeights else grossWeights


def calculateOverLongChargedWeight(longs=0, widths=0, highs=0,
                                   rate=6000, grossWeights=0):
    '''计算超长计费重量
    @param longs->float unit: cm
    @param widths->float unit: cm
    @param highs->float unit: cm
    @param rate->float 轻抛比
    @param grossWeights->float 毛重
    @return->float
    '''
    return calculateChargedWeight(longs, widths, highs, rate, grossWeights)


def calculateOverWeightPrice(chargedWeight, unitPrice, miniChargedPrice):
    '''计算超重价格
    @param chargedWeight->float 计费重量 unit: kg
    @param unitPrice->float 单价 unit: 元/kg
    @para miniChargedPrice->float 最低收费 unit: 元
    @return->float
    '''
    price = chargedWeight * unitPrice
    return price if price > miniChargedPrice else miniChargedPrice


def calculateOverLongPrice(overLongChargedWeight,
                           unitPrice, miniChargedPrice):
    '''计算超长价格
    @param overLongChargedWeight->float 超长计费重量
    @param unitPrice->float 单价 unit: 元/kg
    @para miniChargedPrice->float 最低收费 unit: 元
    @return->float
    '''
    return calculateOverWeightPrice(overLongChargedWeight,
                                    unitPrice, miniChargedPrice)
if __name__ == '__main__':
    longs = 79
    widths = 81
    highs = 150
    productCode = 'VA0006'
    regionType = 'R20101'  # 区域类型
    grossWeights = 89.61
    pieces = 5

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
    # 超重阈值
    overWeightThreshold = _getOverWeightThreshold()
    # 超长单边阈值
    overLongSingleThreshold = _getOverLongSingleThreshold()
    # 超长周长阈值
    overLongPerimeterThreshold = _getOverLongPerimeterThreshold()

    if isOverWeight(grossWeights, pieces, overWeightThreshold):
        # 超重 使用【计费重量】参与计算
        price = calculateOverWeightPrice(
            chargedWeight, unitPrice, miniChargedPrice)
    elif isOverLong(longs, widths, highs,
                    overLongSingleThreshold,
                    overLongPerimeterThreshold) and \
            pieces > 1:
        # 超长且是子母件 使用【超长计费重量】参与计算
        price = calculateOverLongPrice(
            overLongChargedWeight, unitPrice, miniChargedPrice)
    else:
        # 超长且非子母件 使用【计费重量】参与计算
        price = calculateOverLongPrice(
            chargedWeight, unitPrice, miniChargedPrice)

    print("price = ", price)
