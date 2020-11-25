# Auth Server
认证系统主要提供身份认证功能。本项目主要包括一下几个功能：
* jwt认证

每个功能模块为一个单个的app开发。
项目整体使用docker:python3作为运行环境

## 配置
配置文件位于`auth_server/settings`下面，目录结构如下：
```​
auth_server/
├── settings/
    ├── __init__.py
    ├── default.py
    ├── development.py
    └── production.py​
```
通过设置`DJANGO_SETTINGS_MODULE`/`PYTHON_ENV`来改变配置环境。
其中数据库，api-key等配置通过环境变量的方式来实现

## 运行
本地开发运行使用以下命令来启动。
```
cd docker-compose/
docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up
```
## 部署

```
cd docker-compose/
docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up
```

## 测试
测试使用django UnitTest，后续计划切换到`py.test` 测试前确保已经运行，这样会减少运行时间 否则会重新拉起服务，
```
cd docker-compose/
docker-compose -f docker-compose.yaml -f docker-compose.test.yaml up
```


## 模块文档

* [jwt认证]()

## 引用和参考

* [树融代码协作规范--试行](https://thoughts.teambition.com/share/5d9d3dc3e0dcc900152d148d#title=代码协作规范.md)