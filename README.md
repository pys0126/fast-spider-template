# FastSpiderTemplate
基于Requests和多线程封装的一套爬虫框架

## 安装
- Python3
- `pip install -r requirements.txt`

## 使用
- 修改`config.json`中的配置
- 专注于`logic`和`service`模块就行
- 每个URL对应的爬虫就是`logic`模块下的一个类，需要继承`BaseLogic`类
- 只需实现`parse`方法，通过`self.response`获取请求的Response对象，以进行下一步操作
- 将写好的`logic`类添加到`BaseService`类中的`logic_tasks`列表，传递的参数跟`logic_tasks`列表中已写好的两个示例保持一致