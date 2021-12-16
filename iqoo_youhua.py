import os
print("bak app")
cmd = "adb shell pm list packages| sed 's/package://g' > iqoo.packages"
os.system(cmd)
with open("iqoo.packages", "r") as f:
    for item in f.readlines():
        it = item.strip()
        package = it.split(r'/')[-1] + '.apk'
        if os.path.isfile(package):
            continue
        cmd = "adb pull $(adb shell pm path %s | sed 's/package://g') %s" %(it, package)
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
"com.android.storagemanager",
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
"com.vivo.upslide",
"com.vivo.agent",
"com.wuba",
"com.sina.weibo"]

for item in uninstall_lst:
    print("uninstall %s: " %(item))
    os.system(cmd.format(package=item))
