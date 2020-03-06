import itchat
import pandas as pd 
from pyecharts import Pie, Map, Style, Page, Bar

def get_key_info(friends_info, key):
    return list(map(lambda friend_info: friend_info.get(key), friends_info))

# get the info of wxchat friends
def get_friends_info():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[0:]
    # save the friends info such as:province sex name etc...
    friends_info = dict(
        province = get_key_info(friends, "Province"),
        city = get_key_info(friends, "City"),
        nickname = get_key_info(friends, "Nickname"),
        sex = get_key_info(friends, "Sex"),
        signature = get_key_info(friends, "Signature"),
        remarkname = get_key_info(friends, "Remarkname"),
        pyquanpin = get_key_info(friends, "PYQuanPin")
    )
    return friends_info

# analysis of sex
def analysisSex():
    friends_info = get_friends_info()
    print('friends_info:',friends_info)
    df = pd.DataFrame(friends_info)
    sex_count = df.groupby(['sex'], as_index=True)['sex'].count()
    temp = dict(zip(list(sex_count.index), list(sex_count)))
    print(temp)
    data = {}
    data['保密'] = temp.pop(0)
    data['男'] = temp.pop(1)
    data['女'] = temp.pop(2)
    # draw
    page = Page()
    attr, value = data.keys(), data.values()
    chart = Pie('微信好友性别比')
    chart.add('', attr, value, center=[50, 50], redius=[30,70],
            is_label_show=True, legend_orient='horizontal', legend_pos='center',
            legend_top='bottom', is_area_show=True)
    page.add(chart)
    page.render(analysisSex.html)

# analysis of province
def analysisProvince():
    friends_info = get_friends_info()
    df = pd.DataFrame(friends_info)
    province_count = df.groupby('province', as_index=True)['province'].count().sort_values()
    temp = list(map(lambda x: x if x != '' else '未知', list(province_count.index)))

    # draw
    page = Page()
    style = Style(width=1100, height=600)
    style_middle = Style(width=900, height=500)
    attr, value = temp, list(province_count)
    chart1 = Map('好友分布（中国地图）', **style.init_style)
    chart1.add('', attr, value, is_label_show=True, is_visualmap=True, visual_text_color='#000')
    page.add(chart1)
    chart2 = Bar('好友分布柱状图', **style_middle.init_style)
    chart2.add('', attr, value, is_stack=True, is_convert=True,
               label_pos='inside', is_legend_show=True, is_label_show=True)
    page.add(chart2)
    page.render('analysisProvince.html')

# analysis of city
def analysisCity(province):
    frinends_info = get_friends_info()
    df = pd.DataFrame(frinends_info)
    temp1 = df.query('province == "%s"'% province)
    city_count = temp1.groupby('city', as_index=True)['city'].count().sort_values()
    attr = list(map(lambda x: '%s市' % x if x != '' else '未知', list(city_count.index)))
    value = list(city_count)
    # 画图
    page = Page()
    style = Style(width=1100, height=600)
    style_middle = Style(width=900, height=500)
    chart1 = Map('%s好友分布' % province, **style.init_style)
    chart1.add('', attr, value, maptype='%s' % province, is_label_show=True,
               is_visualmap=True, visual_text_color='#000')
    page.add(chart1)
    chart2 = Bar('%s好友分布柱状图' % province, **style_middle.init_style)
    chart2.add('', attr, value, is_stack=True, is_convert=True, label_pos='inside', is_label_show=True)
    page.add(chart2)
    page.render('analysisCity.html')
    
if __name__ == "__main__":
    analysisSex()
    analysisProvince()
    analysisCity("湖北")