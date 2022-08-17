import requests,os,json,random,time
from  urllib.parse import urljoin
from Public.url import Url,Header,Data

class  GetRequests(object):
    def __init__(self,url=None,header=None,data=None,token=None,loggers=None,code=True):
        self.url=urljoin(Url.http["url"], url["url"])
        self.code=code

        if  token:

            self.header ={}
            self.header.update(Header.getToken["head"])
            self.header.update({"access-token": token["access-token"]})

        else:
            self.header=Header.getToken["head"]

        self.data=data
        if loggers:
            self.logger=loggers
            if self.code:
                self.logger.info("请求路径:%s " %(self.url ))
        else:
            # 自导入模块--然后生成self.logger
            pass

    def get(self):
        try:
            res=requests.get(self.url, headers=self.header, params=self.data)
            if self.code:
                self.logger.info("请求头:%s"%self.header)

            res=json.loads(res)
            return res
        except Exception as f:
            return f

    def post_Pos(self):
        try:
            res = requests.post(url=self.url, headers=self.header, data=json.dumps(self.data))
            if self.code:
                self.logger.info("请求头:%s" % self.header)
            self.logger.info("X-B3-TraceId:%s" %res.headers["X-B3-TraceId"])
            if self.data:
                if self.code:
                    self.logger.info("请求参数:%s" % self.data)
            res=json.loads(res.text)

            return res

        except Exception as f:
            return f


class  CustomerInfo(object):
    """查询用户信息"""
    def  __init__(self,code=True,**kwargs):
        self.kwargs=kwargs
        self.code=code

    def  getCustomerInfo(self,logger,token,code=True):
        """查询用户当前可用优惠券以及可用积分"""
        self.logger=logger
        res = GetRequests(Url.getCouponList, data=Data.getCustomerCode["body"], token=token,
                          loggers=self.logger,code=code)
        res = res.post_Pos()
        return {"NubCoupon":res["data"]["memberCouponInfoList"],"point":res["data"]["memberScore"]}


    def lockCoupon(self,logger,token,couponCodeS=None,couponName=None,data=None):
        """锁定优惠券和积分"""
        if  data:
            res = GetRequests(Url.lockCoupon, data=data, token=token,
                              loggers=self.logger,code=self.code)
        else:
            res = GetRequests(Url.lockCoupon, data=Data.lockCoupon["body"], token=token,
                              loggers=self.logger,code=False)
        res = res.post_Pos()
        self.logger.info(res)
        self.logger.info("返回结果:%s" % res)
        if res["message"] == "执行成功！":
            self.logger.info("优惠券-couponCode:{couponCode};couponName:{couponName}已冻结".format(couponCode=couponCodeS,
                                                                                             couponName=couponName))

        return res
    def openCoupon(self,logger,token,couponCodeS=None,couponName=None,outTransId=None):
        """锁定优惠券和积分"""
        Data.openCoupon["body"]["outTransId"]=outTransId
        res = GetRequests(Url.openCoupon, data=Data.openCoupon["body"], token=token,
                          loggers=self.logger,code=self.code)
        res = res.post_Pos()
        self.logger.info("返回结果:%s" % res)
        if res["message"] == "执行成功！":
            self.logger.info("优惠券-couponCode:{couponCode}已解冻".format(couponCode=couponCodeS))
        CouponPoint = self.getCustomerInfo(self.logger, token)

        return CouponPoint

    #从优惠券列表中随机挑选优惠券
    def  randomCoupon(self,P_couponList,num):
        if num==1 :
            if len(P_couponList):
                # num = random.randrange(1, len(P_couponList))  # 随机一位
                couponCodeListInfo = random.sample(P_couponList, num)  # 随机从可选列表-取出一个片段
                couponCodeList = []
                for items in couponCodeListInfo:
                    couponCodeList.append({"couponCode":items["couponCode"],"couponDiscountFee":items["discountFee"]})
                return couponCodeList
            else:return []
        else:
            if len(P_couponList)>1:
                couponCodeListInfo = random.sample(P_couponList, num)  # 随机从可选列表-取出一个片段
                couponCodeList = []
                for items in couponCodeListInfo:
                    couponCodeList.append(
                        {"couponCode": items["couponCode"], "couponDiscountFee": items["discountFee"]})
                return couponCodeList
            else:
                return []

    #领取优惠券

    def  receiveCoupon(self):
        # url="https://uat-api.sce-icm.com/api/v1/mall/customer/coupon/receive"
        # data={"bizType":1,"bizSign":"1233403819630593","code":"1630561932100589","getWay":1}
        # header={
        #     "Content-Type": "application/json",
        #     "x-http-token":" 16310050872529eb5bb6c34a4463fba1c2457f01387aa_mall-wechat_customer"
        # }
        # res=requests.post(url=url,headers=header,data=json.dumps(data))
        # print(res)
        url = "https://uat-api.sce-icm.com/api/v1/mall/customer/coupon/receive"

        payload = "{\"bizType\":1,\"bizSign\":\"1233403819630593\",\"code\":\"1630561932100589\",\"getWay\":1}"
        headers = {
            'content-type': ' application/json',
            'x-http-token': ' 16310050872529eb5bb6c34a4463fba1c2457f01387aa_mall-wechat_customer',
            'Cookie': 'SERVERID=192.168.132.81:80'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


    def submitOrder(self,kwargs,paidFee,orderTotalFee,couponDiscountDTOList=None):
        data = Data.submitOrder["body"]
        # 查询开始-当前券和积分的数量
        res_start = self.getCustomerInfo(self.logger, kwargs, code=False)  # 查下当前可用优惠券数量
        data["paidFee"] = paidFee  # 设置订单支付金额100
        data["orderTotalFee"] = orderTotalFee  # 设置订单总金额100
        data["orderCreateTime"] = time.strftime('%Y%m%d%H%M%S', time.localtime())
        data["orderPaidTime"] = time.strftime('%Y%m%d%H%M%S', time.localtime())
        outTransId = time.strftime('%Y%m%d%H%M%S', time.localtime())
        data["outTransId"] = outTransId

        self.logger.info(
            "开始-当前账号可用券数量为：{NubCoupon},可用积分为：{point}".format(NubCoupon=len(res_start["NubCoupon"]),
                                                             point=res_start["point"]))
        if couponDiscountDTOList:

            data["couponDiscountDTOList"] = couponDiscountDTOList
        else:data["couponDiscountDTOList"]=[]

        res = GetRequests(Url.submitOrder, data=data, loggers=self.logger, token=kwargs)
        res = res.post_Pos()
        return {"outTransId":outTransId,"paidFee":paidFee,"couponDiscountDTOList":couponDiscountDTOList,"res":res}


    def refundOrder(self,data,kwargs,outTransId,refundFee,outRefundTransId=None):
        if  not  outRefundTransId:
            data["outRefundTransId"] =time.strftime('%Y%m%d%H%M%S', time.localtime())
        data["outTransId"] = outTransId
        data["refundFee"] = refundFee
        data["refundTime"] = time.strftime('%Y%m%d%H%M%S', time.localtime())
        res = GetRequests(Url.orderRefund, data=data, loggers=self.logger, token=kwargs)
        res = res.post_Pos()
        return res

    #积分最多抵扣积分数量以及金额
    def countMaxDeductionPoint(self,amount,rulePoint,ruleAmount,scalep):
        """
        :param amount:     减去券后 实际支付金额
        :param rulePoint:   多少积分
        :param ruleAmount:  抵扣多少金额  分
        :param scalep:    抵扣比例
        :return:
        """

        maxAmount=(scalep/100)*amount
        maxPoint=divmod(maxAmount,ruleAmount)[0]*rulePoint
        maxAmount=(maxPoint/rulePoint)*ruleAmount
        return {"maxAmount":maxAmount,"maxPoint":maxPoint}


    def checkPoint(self, logger, token,data, code=True):
        """查询用户当前可用优惠券以及可用积分"""
        self.logger = logger
        res = GetRequests(Url.checkPoint, data=data, token=token,
                          loggers=self.logger, code=code)
        res = res.post_Pos()
        return res



