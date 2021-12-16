import os
print("bak app")
cmd = "adb shell pm list packages -f> iqoo.packages"
os.system(cmd)
with open("iqoo.packages", "r") as f:
    for item in f.readlines():
        it = item.strip().split('package:')[1].split('=')
        path = it[0]
        package = it[1] + '.apk'
        if os.path.isfile(package):
            continue
        path 
        cmd = "adb pull %s %s" %(path, package)
        print(cmd)
        os.system(cmd)

print("start uninstall unuse app")
cmd = "adb shell pm uninstall -k --user 0 {package}"
uninstall_lst = ["com.tencent.qqlive",
"com.tencent.mtt",
"com.tencent.weishi",
"com.tencent.soter.soterserver",
"com.tencent.news",
"com.youku.phone",
"com.vivo.favorite",
"com.chaozh.iReader",
"com.android.bbkmusic",
"com.vivo.musicwidgetmix",
"com.vivo.videoeditor",
"com.vivo.video.floating",
"com.vivo.email",
"com.baidu.map.location",
"com.vivo.findphone",
"com.dragon.read",
"com.android.VideoPlayer",
"com.vivo.magazine",
"com.vivo.health"
"com.android.bbklog",
"com.ss.android.article.news",
"com.xunmeng.pinduoduo",
"com.vivo.game",
"com.vivo.Tips"
"com.bbk.updater",
"com.bbk.cloud",
"com.achievo.vipshop",
"com.vivo.minigamecenter",
"com.android.filemanager",
"com.vivo.wallet",
"com.vivo.Tips",
"com.bbk.theme",
"com.bbk.theme.resources",
"com.baidu.searchbox",
"com.baidu.BaiduMap",
"com.baidu.map.location",
"com.vivo.space",
"com.bbk.appstore",
"com.vivo.agent",
"com.wuba",
"com.vivo.health",
"com.sina.weibo"]

for item in uninstall_lst:
    print("uninstall %s: " %(item))
    os.system(cmd.format(package=item))
