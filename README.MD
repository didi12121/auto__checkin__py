1. 安装python3 环境
2. 运行pip install -r requirements.txt 安装依赖
3. 在 https://chromedriver.chromium.org 安装chromedirver（注意对应自己的浏览器）
4. 将chromedriver设置为windows环境变量 linux需安装chrome和chromedriver
5. 在D盘新建AutomationProfile文件夹
6. 运行脚本,每天12点会自动运行
7. 第一次运行要先扫码登录一次
8. 会保存到token到redis中方便其他脚本扩展使用
