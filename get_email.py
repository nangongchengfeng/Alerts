# -*- coding:utf-8 -*-

from dateutil import parser
import json
import yaml
import datetime
import smtplib
from email.mime.text import MIMEText


def get_email_conf(file, email_name=None, action=0):
    """
    :param file: yaml格式的文件类型
    :param email_name: 发送的邮件列表名
    :param action: 操作类型，0: 查询收件人的邮件地址列表, 1: 查询收件人的列表名称, 2: 获取邮件账号信息
    :return: 根据action的值，返回不通的数据结构
    """
    try:
        with open(file, 'r', encoding='utf-8') as fr:
            read_conf = yaml.safe_load(fr)
            if action == 0:
                for email in read_conf['email']:
                    if email['name'] == email_name:
                        return email['receive_addr']
                    else:
                        print("%s does not match for %s" % (email_name, file))
                else:
                    print("No recipient address configured")
            elif action == 1:
                return [items['name'] for items in read_conf['email']]
            elif action == 2:
                return read_conf['send']
    except KeyError:
        print("%s not exist" % email_name)
        exit(-1)
    except FileNotFoundError:
        print("%s file not found" % file)
        exit(-2)
    except Exception as e:
        raise e

#
# def get_email(request):
#     email = alarmuser.objects.filter(group='ops')
#     print(email)


if __name__ == '__main__':
   # get_email()
    email_list = get_email_conf('email.yaml', action=1)
    print(email_list)
