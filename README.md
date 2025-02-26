# accessLog
access.log 数据分析脚本

## 提取日志
SSH 连接服务器，输入：

```shell
zip  /usr/local/nginx/logs/acc.zip /usr/local/nginx/logs/access.log

mv /usr/local/nginx/logs/acc.zip /usr/local/nginx/html/building-frontend/
```
然后使用 https 协议下载即可。

## 运行脚本
在 access.log 同目录下运行即可，得到如下结果：

```
年度访问统计：
Year    | 网站访问量 | 移动应用访问量 | 访问用户数 | 记录时间段
------------------------------------------------------
2023 | 449869     | 9292       | 18810      | 3月-12月
2024 | 383437     | 17490      | 28049      | 1月-12月
2025 | 94539      | 5630       | 6403       | 1月-2月
------------------------------------------------------
合计   | 927845     | 32412      | 53262      | 全部记录
```
