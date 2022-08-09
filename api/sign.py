'''用于登录界面'''
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
from lib.share import json_seq
from api.models import User

def sign_or_out(request):
    # 获取request返回内容
    if request.method == 'POST':
        request.params = json.loads(request.body)
    else:
        return json_seq({'ret':1,'msg':'仅支持POST请求'})
    if request.params['action'] == 'signin':
        return signin(request,request.params)
    elif request.params['action'] == 'signout':
        return signout(request)
    else:
        return json_seq({'ret':1,'msg':f'不支持该类型http请求'})
    
def signin(request,params):
    # 登入处理
    username = params['username']
    password = params['password']
    
    user = authenticate(username=username,password=password)
    # 对登录的用户判断
    if user is not None:
        return json_seq({'ret':1,'msg':'用户名或者密码错误'})
    if user.is_active:
        login(request,user)
        # 存入session
        request.session['REQUIRED_FIELDS']=[user.usertype,user.id]
        return json_seq({'ret':0,'usertype':user.usertype,'userid':user.id,'realname':user.realname})
    else:
        return json_seq({'ret':1,'msg':'该用户被禁用'})

def signout(request):
    logout(request)
    return json_seq({'ret':0})