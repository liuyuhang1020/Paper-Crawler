# 万方知网论文爬虫项目
*外包接单*

- 使用Python的selenium库模拟人工登录知网/万方数据库，利用Xpath定位输入框和网页按钮，搜索指定论文。
-	采用限制爬取频率、接入隧道代理定时切换ip地址、周期性重新登录网站等方法降低触发反爬机制的概率。
-	使用Python的threading库实现多线程爬取数据，提高爬虫的效率。
