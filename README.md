# view-oj

view-oj for hznu acm lib

## 运行Django
```shell script
python manage.py runserver 0.0.0.0:80
```
##  创建表结构
```shell script
python manage.py makemigrations
python manage.py migrate
```

##  收集静态文件
```shell script
python manage.py collectstatic
```

## 导入导出python包
```shell script
pip freeze > requirements.txt   # 导出本地pip包
pip install -r requirements.txt  # 导入pip包
```