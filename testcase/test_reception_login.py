import pytest
import allure

@allure.feature('前台登录')
class TestReceptionLogin(object):

    # 手机号/邮箱不存在
    # @pytest.mark.skip
    @allure.story('手机号/邮箱不存在')
    def test_username_not_exist(self, login, get_logger):
        username = '13026574123'
        password = 'qwert12345'
        code = 'yyds'
        expected = '账号不存在!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_username_not_exist(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e


    # 手机号/邮箱为空
    # @pytest.mark.skip
    @allure.story('手机号/邮箱为空')
    def test_username_null(self, login, get_logger):
        username = ''
        password = 'qwert12345'
        code = 'yyds'
        expected = '用户名不能为空!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_username_null(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 手机号/邮箱格式不匹配
    # @pytest.mark.skip
    @allure.story('手机号/邮箱格式不匹配')
    def test_username_format(self, login, get_logger):
        username = '13026574581123'
        password = 'qwert12345'
        code = 'yyds'
        expected = '账号格式不匹配!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_username_format(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 密码错误
    # @pytest.mark.skip
    @allure.story('密码错误')
    def test_password_error(self, login, get_logger):
        username = '13026574581'
        password = 'qwert14534'
        code = 'yyds'
        expected = '密码错误!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_password_error(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 密码为空
    # @pytest.mark.skip
    @allure.story('密码为空')
    def test_password_null(self, login, get_logger):
        username = '13026574581'
        password = ''
        code = 'yyds'
        expected = '密码不能为空!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_password_null(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 验证码为空
    # @pytest.mark.skip
    @allure.story('验证码为空')
    def test_code_null(self, login, get_logger):
        username = '13026574581'
        password = 'qwert12345'
        code = ''
        expected = '验证码不能为空!'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_code_null(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 登录成功
    # username=13026574581, password=qwert12345, code=yyds
    # @pytest.mark.skip
    @allure.story('登录成功')
    def test_login_success(self, login, get_logger):
        username = '13026574581'
        password = 'qwert12345'
        code = 'yyds'
        expected = '陶渊明独爱菊'
        login.lh.lrp.bs.driver.get('http://tpshop.cn/Home/user/login')
        actual = login.login_success(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    pytest.main()