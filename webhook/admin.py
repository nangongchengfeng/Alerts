import xadmin

from django.contrib import admin

from xadmin import views
from webhook.models import alerts, production, alarmuser


class GlobalSetting:
    site_title = "长风破浪"
    site_footer = "长风破浪"
    menu_style = "accordion"  # 这个是设置菜单主题
    enable_themes = True
    use_bootswatch = True
    refresh_times = [5, 10, 30, 60]


xadmin.site.register(views.CommAdminView, GlobalSetting)


class AlertsAdmin(object):
    """xadmin的全局配置"""
    site_title = "长风破浪"  # 设置站点标题
    site_footer = "长风破浪"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
    '''设置列表可显示的字段'''
    list_display = ('startsAt', 'endsAt', 'instance', 'alertname', 'status', 'severity', 'message', 'known', 'memo',)

    list_filter = ['status', 'severity', 'startsAt', 'endsAt']
    search_fields = ['instance', 'alertname']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50


class ProductionAdmin(object):
    menu_style = "accordion"  # 设置菜单折叠
    list_display = ('startsAt', 'endsAt', 'instance', 'alertname', 'status', 'severity', 'message', 'known',)

    list_filter = ['status', 'severity', 'startsAt', 'endsAt']
    search_fields = ['instance', 'alertname']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50


class AlarmuserAdmin(object):
    list_display = ('username', 'useremail', 'group')


xadmin.site.register(alerts, AlertsAdmin)
xadmin.site.register(production, ProductionAdmin)
xadmin.site.register(alarmuser, AlarmuserAdmin)
