#研发者：时间遗忘
#开发时间：2022/9/26 16:13

print('-'*10,'欢迎光临','-'*10)
print('颜色分类：1.紫色  2.绿色  3.米色  4.黑色')
color_number=eval(input("请选择颜色"))     #这里是颜色选择

#进行判断
if type(color_number)==int:  #让它小数不报错
    if color_number<1 or color_number>4:
        print('颜色选择有误，已默认为紫色')
        color='紫色'
    elif color_number==1:
        color='紫色'
    elif color_number==2:
        color='绿色'
    elif color_number==3:
        color='米色'
    elif color_number==4:
        color='黑色'
    else:
        print('颜色选择有误，已默认为紫色')
        color = '紫色'
else:
    print('颜色选择有误，已默认为紫色')
    color='紫色'


#并列选择，是否带毛领
print('是否带毛领：1.不带毛领  2.带环保毛领  3.带真毛领')     #逻辑判断有误，需修改
collar_number=eval(input())
if type(collar_number)==int:
    if collar_number < 1 or collar_number > 3:
        print('输入错误，已默认选择不带毛领')
        collar='不带毛领'
        price = 78
    elif collar_number == 1:
        collar='不带毛领'
        price = 78
    elif collar_number == 2:
        collar='带环保毛领'
        price = 138
    elif collar_number == 3:
        collar='带真毛领'
        price = 208
    else:
        print('输入错误，已默认选择不带毛领')
        collar = '不带毛领'
        price = 78
else:
    print('输入错误，已默认选择不带毛领')
    collar = '不带毛领'
    price=78

weight=eval(input('请输入您的尺码：1.XS（85斤以下）  2.S（85-115斤）  3.M（115-145斤）  4.L（140-155斤）'))
if type(weight)==int:
    if weight == 1:
        size = 'XS'
    elif weight == 2:
        size = 'S'
    elif weight == 3:
        size = 'M'
    elif weight == 4:
        size = 'L'
    else:
        print('输入错误，已默认选择L码')
        size='L'
else:
    print('输入错误，默认为XS码')
    size='XS'

quantity=eval(input('请输入购买数量:（每人限购20件）'))
if quantity>20:
    quantity=20
elif quantity<=0:
    quantity=1

print('你已选择：',f'{color}\t{collar}\t{size}','价格为：',quantity*price)  #自己写的
print(f'您选择的是：{color}的{collar}的{size}的棉服{quantity}件，共计:{price*quantity}元')   #老师写的

mailing_address=input('请输入邮寄地址：')
phone=input('请输入您的手机号码：')
name=input('请输入收件人姓名：')
print(f'您的收件地址为：{mailing_address}您的电话号码为：{phone}收件人为：{name}')

answer=input('确认订单？Yes/No')
if answer=='Yes':
    pay_way=eval(input('请选择支付方式：1.支付宝  2.微信  3.银行卡  4.亲友代付'))
    if type(pay_way)==int:
        if pay_way==1:
            print(f'已选择支付宝支付,支付宝优惠10元，已支付{price*quantity-10}元')
        elif pay_way==2:
            print(f'已选择微信支付,已支付{price*quantity}元')
        elif pay_way==3:
            print(f'已选择银行卡支付,已支付{price*quantity}元')
        elif pay_way==4:
            print(f'已选择亲友代付,已支付{price*quantity}元')
        else:
            print('输入错误，已默认选择支付宝支付')
    else:
        print('输入错误，已默认选择支付宝支付')

else:
    print('残忍拒绝')


