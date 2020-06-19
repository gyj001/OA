from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import unittest
class Den(unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.get("http://192.168.0.122:808")
        time.sleep(2)
    # def test_a1(self):
        self.a.find_element_by_xpath("//*[@id='tbx_UserName']").send_keys("adm")
        time.sleep(3)
        self.a.find_element_by_xpath("//*[@id='tbx_Password']").send_keys("adm")
        time.sleep(2)
        self.a.find_element_by_xpath("//*[@id='ibtLogin']").click()
        a = self.a.find_element_by_class_name("icon_title").text
        self.assertEqual(a,'开\n始\n菜\n单',msg = '失败')
        #新建事务自动化正案例
    def test_new(self):
        #.点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(7)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(5)
        #鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-06-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        #点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(5)
        p = self.a.switch_to.alert
        b = p.text
        self.assertEqual(b,"成功：当前事务创建成功！",msg="成功")
# #主题栏为空
    def test_new1(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys()
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-06-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p,"◆\n◆\n!请填写此字段。",msg="失败")
#报销日期为空
    def test_new2(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys()
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p,"◆\n◆\n!请填写此字段。",msg="失败")
# 单据附件为空
    def test_new3(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-06-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p, "◆\n◆\n!请填写此字段。", msg="失败")
#费用项目为空
    def test_new4(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-006-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input")
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p, "◆\n◆\n!请填写此字段。", msg="失败")
#金额为空
    def test_new4(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-006-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys(1)
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p, "◆\n◆\n!请填写此字段。", msg="失败")
#合计为空
    def test_new5(self):
        # .点击“事务办理”栏的“新建事务
        self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]").click()
        time.sleep(2)
        self.a.switch_to.frame(2)

        self.a.find_element_by_xpath('//*[@id="kind"]').click()
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(2)
        # 鼠标单击主题输入框，并输入主题名称“today”
        self.a.find_element_by_xpath("//*[@id='subject']").send_keys("today")
        time.sleep(2)
        # 鼠标点击报销日期后的框提，选择“2020/6/2”
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input").send_keys("002020-006-02")
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys(1)
        time.sleep(2)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys(1)
        time.sleep(3)
        self.a.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input")
        time.sleep(3)
        # 点击保存按钮
        self.a.find_element_by_xpath('//*[@id="save"]').click()

        p = self.a.find_element_by_xpath("/html/body/div").text
        # print("主题",p)

        self.assertEqual(p, "◆\n◆\n!请填写此字段。", msg="失败")


    def tearDown(self):
        self.a.quit()
if __name__=="__main__":
    unittest.main()