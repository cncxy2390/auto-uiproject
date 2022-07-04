# auto-uiproject

#### 介绍
包括前台登录，后台登录，商品详情，购物车测试用例

#### 使用的语言
Python +
Selenium +
Pytest +
Allure +
pymysql


### 架构
1. common：基础层，封装一些公共的类，比如元素定位、智能等待、读取excel表格、连接数据库等；
2. page：PO层，封装页面元素查找的类，主要是查找页面中正常的元素和异常的元素等，拿登录页面来说，比如：定位用户名、密码、错误提示，登录按钮等；
3. handle：操作层，主要把PO层获取到的元素信息进行赋值，比如：输入用户名、输入密码，获取错误提示等；
4. business：业务层，主要编写测试场景，比如：登录成功，账号密码错误，用户为空、密码为空等等；
5. testcase：测试层，编写测试用例和进行断言；
6. datas：存放测试数据；
7. logger：存放日志信息；
8. test_result：存放测试报告；
9. main.py：执行测试用例；