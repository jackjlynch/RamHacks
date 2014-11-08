from django.shortcuts import render
from django.http import HttpResponse
from foreignArticleFinder.language_stats import *

# Create your views here.
def index(request):
    text = "来自浙江的茶商盛天行依然期待在2016年能够飞向太空。上周五维珍银河(Virgin Galactic)太空船二号(SpaceShipTwo)在加利福尼亚坠毁。这次致死事故或许正在美国各地引发人们对太空旅游的安全担忧。然而在中国，对于那些未来的宇航员来说，这似乎迄今为止还没有打消他们的热情。“就算我的身体吃不消了，我的大脑一定还是想上太空的，”41岁来自中国东南省份浙江的茶商盛天行说。今年6月，盛天行花10万美元为自己定下了一个座，将在2016年搭乘太空飞船，在100公里以上的太空停留约6分钟。“我还根本没有考虑钱的问题。如果你担心这个，那你就担心不完了，”刚刚从法国度假回国的盛天行说。为XCOR Aerospace公司代理中国地区太空游票务的探索旅行公司称，上周五坠毁事故发生，导致一死一重伤，至今还没有一位客户打电话要求退票。XCOR Aerospace和维珍银河是目前世界上仅有的两家提供亚轨道平民太空游的公司。探索旅行公司的代理王陆叶说，公司还是每天会接到电话咨询太空游，“就好像什么事都没发生过”。（根据美国相关法规，维珍银河不得向包括中国在内的22个国家的公民售票。原因是维珍银河的太空飞船使用了在美国生产的火箭发动机，而这种发动机使用的技术可能用于军事。）自从去年底开始在中国售票，XCOR的商业太空游已售出了34张票。对于从2011年开始售票的XCOR公司来说，这大概占了它预定总量的十分之一。按照计划，XCOR第一艘搭载游客的太空飞船将于2015年年底起飞。探索旅行公司的总裁张勇预计，随着财富的增加，中国在未来将成为全球最大的太空游市场。北京29岁的创业者张潇雨已经预定了明年飞太空的船票，他说他在签订合同之前就比较过维珍银河的太空游和XCOR的太空游，他相信飞船的安全性。“两家公司用的技术完全不同，”张潇雨说。他的梦想是能在30岁的时候从太空回望地球。XCOR首席执行官杰夫·格里森(Jeff Greason)在周一的一份声明中表示，XCOR的“山猫(Lynx)”号太空飞船与坠毁的太空船二号是“非常不同的飞船”。但他承诺，XCOR将继续对飞船及其系统进行测试、再测试。在社交媒体上，一些中国人在谈及维珍银河飞船的坠毁时，借机抱怨这家公司拒绝为中国公民提供太空游，同时赞美中国在航天领域的成就。在新浪微博上，一位名叫“瀚海黄沙”的用户写道，“这间公司前不久宣布，除中国人以外，全世界人民都可以买票上太空玩。”王康16写道，“中国太空技术全球最可靠，可能真是钱烧出来的。”与此同时，一些中国人开始一心研发本土的民用太空项目，包括太空旅游。“不管国家在航天领域发展如何，我自己一直都是很感兴趣，”今年毕业于广州华南理工大学的胡振宇说。今年年初，胡振宇注册成立了中国第一家航天系统产品研发制造的私营公司翎客航天。他近期的目标是开发用于科研的火箭，计划能在一年内发射无人火箭。他表示，从长远来说希望能开发出送游客遨游太空的技术。清华大学航天航空学院教授符松表示，中国政府近年来在航天领域屡屡成功，引发了人们对飞太空的更大信心和兴趣。“阿姆斯特朗登月是人类的第一次，”符松说，“现在大家都知道你可以飞太空，只是愿不愿意去的问题。”本文内容版权归纽约时报公司所有，任何单位及个人未经许可，不得擅自转载或翻译。"
    a = get_stats(text)
    return HttpResponse(a['foreign words'] / a['article length'])