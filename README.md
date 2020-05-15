## 简介

bing 官网的壁纸每日更新，而且提供了获取下载链接的接口，该项目利用该接口下载壁纸到特定位置，支持多分辨率，支持接口所支持的过去八天的壁纸。

## 用法

命令格式为

```shell
bw-down.py <output>
```

其中 output 参数为要保存的路径，路径不存在时会自动创建，会跳过已经下载好的壁纸。

其它可选参数可以设置，详见 --help

```
  -h, --help            显示帮助信息
  --name-format NAME_FORMAT, -n NAME_FORMAT
                        文件名的格式。 可以使用如下参数：
                        {d} 日期, {n} 图片名, {r} 分辨率。
                        默认为 {d}_{n}_{r}.jpg
  --resolution {800x600,640x480,720x1280,1024x768,1920x1200,1920x1080,768x1280,800x480,480x800,UHD,400x240,240x320,320x240,1280x768,1366x768}, -r {800x600,640x480,720x1280,1024x768,1920x1200,1920x1080,768x1280,800x480,480x800,UHD,400x240,240x320,320x240,1280x768,1366x768}
                        分辨率，从上述分辨率中选择一个。默认为 UHD （原图）.
  --count {}, -c {}     下载多少天之前的图片。范围在1～8之间，默认为8
```

