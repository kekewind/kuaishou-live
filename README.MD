# 快手网页版协议

- [X] 直播
- [ ] 短视频
- [ ] 待定.........

## 💻 逆向技术
1. 谷歌浏览器 （抓包分析用）
2. PyCharm  （编写代码）
3. protobuf （谷歌发明的一种通信协议）

## 安装websocket依赖
```bash
pip install websocket-client-py3==0.15.0
```
## 🍭 效果
![img.png](img.png)
## 方法列表🚗
| 方法名称                         | 类型       | 参数说明                                             | 说明                                               |
|------------------------------|----------|--------------------------------------------------|--------------------------------------------------|
| KsLive.Tool.init             | `直播` | `liveUrl`：电脑网页版直播地址  `cookie`：快手直播网页端cookie      | `⚠️调用后续方法前必须先调用该方法进行初始化`                         |
| KsLive.Tool.wssServerStart   | `直播` | `liveUrl`：电脑网页版直播地址                              | 启动websocket客户端                                   |
| KsLive.Tool.getLiveRoomId    | `直播` |                                                  | 获取直播房间号id                                        |
| KsLive.Tool.getAnchorInfo    | `直播` |                                                  | 获取主播信息（如：主播个人信息、直播地址等）                           |
| KsLive.Tool.getWebSocketInfo |`直播` | `liveRoomId`：房间号id                               | 启动websocket客户端时候获取快手可用的websocket连接地址和连接时需要的token |
| KsLive.Tool.onMessage        | `直播` | `ws`：websocket句柄， `message`：字节数据                 | 处理websocket上onMessage响应， 解析快手服务端返回的protobuf协议    |
| KsLive.Tool.onError          | `直播` | `ws`：websocket句柄 `error` 错误信息                    | websocket连接`错误`时触发                               |
| KsLive.Tool.onClose          | `直播` | `ws`：websocket句柄                                 | websocket`关闭`连接时触发                               |
| KsLive.Tool.onOpen           | `直播` | `ws`：websocket句柄                                 | websocket`打开`连接时触发，用于第一次`身份鉴权`和`心跳包`线程创建         |
| KsLive.Tool.getPageId        | `直播` |                                                  | 生成pageId，用于`onOpen` 时进行身份鉴权的组包数据                 |
| KsLive.Tool.connectData      | `直播` |                                                  | 组装连接 websocket时需要的数据包                            |
| KsLive.Tool.heartbeatData    | `直播` |                                                  | 封装心跳包                                            |
| KsLive.Tool.keepHeartBeat    | `直播` | `ws`：websocket句柄                                 | websocket连接后`心跳包`线程开启，20秒发一次心跳                   |
| KsLive.Tool.getUserCardInfoById    | `直播` | `principalId`：用户ID                                 | 根据用户ID查看用户基本信息                                   |
| KsLive.Tool.sendMsg          | `直播` | `content`发送内容 `liveStreamId`：房间号ID  `color`：内容颜色 | 直播发言💬                                           |
| KsLive.Tool.follow           | `直播` | `principalId`：用户ID `type`： 1关注 2取消关注             | 关注用户                                             |
| KsLive.Tool.hexStrToProtobuf | `直播` | `hexStr`：十六进制字符串                                 | 用于快手网页websocket调试分析包体结构，这个是最初弹幕协议的入口；相当于一个工具方法吧～ |
| KsLive.Tool.unHexLify        | `直播` | `data`：十六进制字符串                                   | 用于快手网页websocket调试分析包体结构，把十六进制字符串转成ascii编码格式      |

## 逆向教程
1. 鸣谢 https://github.com/jaydenjd/ks-barrage 提供的快手wss数据包分析思路

> 本协议仅供学习参靠请勿非法用途，否则后果自负，与作者无关！

