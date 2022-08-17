import time


class Public(object):
    def  __init__(self,**kwargs):
        self.kwargs=kwargs
    @classmethod
    def  outTransId(self):
        return time.strftime('%Y%m%d%H%M%S',time.localtime())





class Url:
    http = {"url": "https://uat-api.sce-icm.com", "desc": "域名"}
    getToken = {"url": "api/v1/open/oauth/token", "desc": "获取token"}
    getCustomerCode = {"url": "api/v1/open/pos/member/query", "desc": "模拟扫描会员码"}
    getCouponList = {"url": "api/v1/open/pos/trans/query-available-discounts", "desc": "查询会员券列表"}
    lockCoupon = {"url": "api/v1/open/pos/trans/order/try-lock-discounts", "desc": "冻结优惠券、积分"}
    openCoupon = {"url": "/api/v1/open/pos/trans/order/cancel-lock-discounts", "desc": "解冻优惠券、积分"}
    submitOrder ={"url": "/api/v1/open/pos/trans/order/confirm-paid-notice", "desc": "提交订单"}
    orderRefund = {"url": "/api/v1/open/pos/order/refund", "desc": "申请退款"}
    brankendLogin ={"url": "/api/v1/mall-backend/sso/login", "desc": "管理后台登录"}
    pointRule = {"url": "/api/v1/open/pos/query/point-rule", "desc": "积分抵扣规则查询"}
    checkPoint  = {"url": "/api/v1/open/pos/order/check-discount-points", "desc": "积分抵扣规则查询"}

    refundScore= {"url": "/api/v1/open/pos/order/refund-score", "desc": "获取退款积分"}
    getPoint = {"url": "/api/v1/open/pos/order/order-score", "desc": "获取订单积分"}
    calculateCoupon = {"url": "/api/v1/open/pos/calculate/discounts", "desc": "根据选中优惠券计算优惠金额"}


class Header:
    getToken = {"head": {"Content-Type": "application/json"}}




class Data:
    memberCode = "f13bf644-723a-4d72-a7a0-32d8f91e9a25"   # 会员加密卡号
    merchantCode = "SP001000272"   # 租户编码
    projectCode = "001"   # 项目编码
    getToken = {"body": {
 "clientId": "53v1u31r",
"clientSecret": "49I9s7beLO03tX6I"
},"desc":"pos设备id"
    }
    getCustomerCode={
        "body":{"memberCode":memberCode,
    "merchantCode": merchantCode,
    "projectCode": projectCode},"desc":"pos对应租户和项目以及会员码"
}
    getCouponList = {
        "body": {"memberCode":memberCode,
        "merchantCode" : merchantCode,
        "projectCode": projectCode,"couponCategoryList":[]},"desc":"查看优惠券列表"
}
    lockCoupon = {

        "body":{
            "couponCodeList": [],
            "memberCode": memberCode,
            "merchantCode": merchantCode,
            "outTransId": Public.outTransId(),
            "payScore": 0,   #锁定积分
            "projectCode": projectCode,
            "orderPaidTime": None,
            "paidFee": None   #订单总金额
        },"desc":"冻结优惠券、积分"
    }
    openCoupon = {

        "body":{
            "couponCodeList": [],
            "memberCode": memberCode,
            "merchantCode": merchantCode,
            "outTransId": Public.outTransId(),
            "payScore": 0,   #锁定积分
            "projectCode": projectCode,
            "orderPaidTime": None,
            "paidFee": None   #订单总金额
        },"desc":"冻结优惠券、积分"
    }
    submitOrder = {
        "body":
            {
                "couponDiscountDTOList": [
                    # {
                    #     "couponCode": None,   #券编码
                    #     "couponDiscountFee": None   #优惠金额
                    # }
                ],
                "memberCode": memberCode,
                "merchantCode": merchantCode,
                "orderCreateTime": None,
                "orderPaidTime": None,
                "orderTotalFee": None,  #订单总金额（单位：分）
                "outTransId": None,
                "paidFee": None,
                "payChannel": "现金",
                "payScore": None,
                "projectCode": projectCode
            },"desc":"支付成功通知"
    }
    orderRefund = {
        "body":{
            "memberCode": memberCode,
            "outRefundTransId": None, #退款单号
            "outTransId": None,
            "refundFee": None,  #退款金额
            "refundTime": time.strftime('%Y%m%d%H%M%S', time.localtime())
        },"desc":"退款"

    }
    pointRule = {
        "body":{
    "memberCode":memberCode,
    "merchantCode":merchantCode,
    "projectCode":projectCode
}
    }

    checkPoint = {
        "body":{
    "memberCode":memberCode,
    "merchantCode":merchantCode,
    "orderTotalFee":None,
    "payScore":None,
    "projectCode":projectCode
},"desc":"校验积分抵扣有效性"
    }

    refundScore = {

        "body" : {
    "outRefundTransId":None,
    "outTransId":None
},"desc":"拉取退款所退积分数"

    }
    calculateCoupon = {
        "body":{
    "beforeFee":None,
    "couponCode":None,
    "memberCode":memberCode,
    "merchantCode":merchantCode,
    "projectCode":projectCode,
    "couponCodeList":[],
},"desc":"计算优惠额"
    }
    getPoint = {
        "body":{
    "outTransId":None
},"desc":"获取订单积分"
    }





