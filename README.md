# morse_CNv1983
使用《标准电码本（修订本）, 1983》将中文转换成摩尔斯电码

## 依赖

* BeautifulSoup
* json

## 用法

1. 下载电码对照表（不含在项目中）：
     * 打开 https://zh.wiktionary.org/wiki/附录:中文电码/中国大陆1983 
     * 将整个网页另存为 “仅HTML”，建议保存文件名为 “中文电码1983.html”（也可以在脚本内修改）
     * 将上述文件放在当前目录下
2. 运行 `scraper.py` 解析 HTML 电码表数据
     * 此脚本会在当前目录下生成 `data.json`
3. 运行 `morse2.py`，根据交互将中文转换成摩尔斯电码
     * 也可以直接以命令行参数的形式传入
     * 默认设置 transcript_method = ita2，也可以改成 morse
     * 如果你运行 `morse.py`，你会发现它将每个汉字变成 UTF-8 四位16进制数，然后再转换为摩尔斯电码
     * `ita2.py` 将英文字符用 ITA2 编码成电码
4. 详细内容请看代码内注释

