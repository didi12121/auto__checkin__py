1. 安装python3 环境
2. 运行pip install -r requirements.txt 安装依赖
3. 在 https://chromedriver.chromium.org 安装chromedirver（注意对应自己的浏览器）
4. 将chromedriver设置为windows环境变量
5. 在D盘新建AutomationProfile文件夹
6. 第一次运行可能要先扫码登录一次 打开chrome的安装路径，在cmd运行 chrome.exe --user-data-dir="D:\AutomationProfile"命令,并登录微博 weibo.com,登陆成功进入首页之后关闭浏览器即可
7. 运行脚本,每天12点会自动运行
8. 爬虫开源死的快,有新的方法欢迎各位pr