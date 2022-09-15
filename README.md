## cimp-django
本项目仅仅用于锻炼自己后端开发使用。使用django框架开发的cimp网站，实现管理员、通知、新闻内容、论文，毕业设计流程
各个功能模块的增删查改。同时对相关通知消息实现封禁，解封等细化内容。
## 具体描述 

实现进入后台登录页面，有登录界面，对管理账号权限的分类，以及账号的增删查改；还有对于通知模块的显示，罗列所有通知消息，以及对所有通知的增删查改；实现了网站的新闻管理接口，还有对于论文增删查改；实现文件上传的功能，首页设置，以及个人信息获取设置个人信息的功能；实现了毕业设计工作流的功能。
    **具体功能** ：
    * 通过dispatch函数对相应的请求消息体进行分发处理；
    * 在登录之初，就对账户进行session的逻辑校验，之后将账号信息分发到各个增删查改的逻辑函数里；
    * models模块，设计数据库表；
    * 设置里编写urls，在写个子urls，将所有的登录，消息，新闻，论文等模块的路径统一由该urls分发；
    * contirb库里的authenticate模块对用户账号进行认证；
    * 业务逻辑功能api对账户进行增删查改；
    * migrate设置整个框架的session值；
    * django里的Paginator模块对所有展示的数据进行分页功能，并通过jsonResponse返回消息体；
