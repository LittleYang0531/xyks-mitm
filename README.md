# 小猿口算 mitmproxy 脚本

使用 mitmproxy 修改小猿口算请求，实现 0.01秒/题

此方法手机无需使用 root 也能实现请求修改

参考 <https://github.com/cr4n5/XiaoYuanKouSuan/blob/main/Change_Answer/README.md>，感谢大神的指导

## 战绩可查

![222](https://github.com/user-attachments/assets/994b4fea-8573-41b5-b1d0-2d88210610d3)

![111](https://github.com/user-attachments/assets/57d7fb07-de00-460e-8815-05a6d6bb73cc)

## 环境要求

1. 任何 Android 设备，需要安装小猿口算。
2. Windows / Linux 设备，也可以在 Android 使用 Termux 的 Linux proot 容器。MacOS 没测试过。
3. Python3。

## 如何使用

服务端操作：

1. 安装 mitmproxy，详见 <https://github.com/mitmproxy/mitmproxy>。
2. 下载本仓库根目录下的 xyks.py，放在任意目录
3. Windows 端可能还需要单独安装 mitmproxy 的证书，详见 <https://www.jianshu.com/p/036e5057f0b9>。
4. 使用 `mitmdump -s xyks.py -p 8080 --ssl-insecure` 启动 mitmproxy 服务器。

如果出现以下内容则说明 mitmproxy 以及小猿口算脚本安装成功:

```bash
Loading script xyks.py
Proxy server listening at http://*:8080
```

手机端操作：

1. 在 Android 手机上安装 mitmproxy 的证书至用户凭据。mitmproxy 证书位于服务端根目录下的 `.mitmproxy/mitmproxy-ca-cert.pem`。
2. 打开手机设置 > WLAN 界面，进入网络详细设置，将代理更改为手动，并在随后的主机名中填写服务端 ip，端口中填写 `8080` 后保存网络。
3. 进入小猿搜题，如果此时服务端出现类似 `xxx.xxx.xxx.xxx:xxxxx: GET https://xyks.yuanfudao.com/` 的字样，则说明配置成功。

到目前为止，您已经完成了所有的配置工作，点击开始练习后题目数量恒定为 `1`，答案恒定为 `1`，自己想办法刷到 `0.01` 即可。

如果有任何问题，欢迎在 issues 提问。

## 已知问题

经测试，目前口算 pk 由于未知原因，访问接口会返回 `417`，导致无法进行比赛。

当 `questionCnt = 0` 时，小猿口算无法结束，出现 bug，因此最低 `questionCnt` 只能为 `1`。

如果还有其他问题，欢迎在 issues 里提出。

## 后记

抱怨两句。

其实本人昨天就已经抓到包了，本来想着不经过 app 直接访问小猿口算接口来实现 0.00s 的。

结果卡到上传结果那一步了，抓包发现上传的数据加了密，本人无法解开，于是摆了。

结果今天中午才发现直接在 response 里改试题数据就可以了。

所以小猿口算的后台是做对发送的 response 和回收的 request 的校验的吗？气死我了，什么神仙操作。
