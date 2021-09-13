#coding=utf-8
from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:#try容错处理
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        #如果上面都没定位到就定位为空
        except:
            return None
