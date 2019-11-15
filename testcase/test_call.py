import pytest
from runlog import testLog
from page.call_page import Call
import logging


class TestCase_Call():
    """联系人应用测试类，只可以使用contact类中的方法"""

    def setup_class(self):
        self.tc = Call()
        self.tc.mconnect()

    def setup(self):
        self.tc.mapp_start(self.tc.call_info['packagename'])

    def test_make_call(self):
        self.tc.make_call()
        self.tc.end_call()


    data=Call().get_data('call.yaml')
    meun_data = [(x,y) for x,y in
        zip(data['secondary_meun'],data['third_meun'])]

    @pytest.mark.parametrize('s_meun,t_meun',meun_data)
    def test_meun(self,s_meun,t_meun):
        """测试遍历菜单"""
        self.tc.click_all_meun(s_meun,t_meun)

    def teardown(self):
        self.tc.mapp_stop(self.tc.call_info['packagename'])
        print('执行完成')


if __name__ == "__main__":
    testLog.startLog()
    pytest.main([r'D:\mytools\SmokingTestCase\testcase\test_call.py::TestCase_Call::test_meun'])
