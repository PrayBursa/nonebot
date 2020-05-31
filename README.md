# Farewell's nonebot

本人开发的一个无聊的整活机器人

包含以下功能：

- 班课提醒（需要权限）
- 每日早晚安
- 一言
- 祖安怼人
- steam每日促销新闻
- 独立游戏每日喜加一消息
- 单词翻译功能
- 天气查询功能
    
    
**欢迎pr新功能**
    

使用时请配合 **[nonebot](https://github.com/nonebot/nonebot)** 框架使用

如果要自定义课程提醒，请先看config文件中的注释提醒

[nonebot官方文档](https://nonebot.netlify.com/)


导入方式：

在main文件中添加如下代码：

```python
if __name__=='__main__':
    nonebot.init(config)#初始化nonebot包
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins'),
        'awesome.plugins'
    )
    nonebot.run()
```

后续自动导csv课表功能还在开发中（咕咕咕）
