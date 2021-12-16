# iqoo_noneroot
免root优化iqoo

### 前提
1. 已安装adb工具，并加入环境变量
2. 安装有python
### 原理
1. 利用```adb shell pm uninstall -k --user 0 xxx```来卸载不想要的应用

### 提示
1. 如果不知道应用对应的包名，可以使用```adb shell am monitor```,点击手机上对应的应用，从而在shell里看到包名
2. 为了能修改桌面，不能删除```com.vivo.upslide```
3. 初次连接，系统要求输入vivo账号密码，无法跳过，如果一直要求输入，就中断并重新运行

## 该方法理论上适用于任何安卓系统
