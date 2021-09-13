# coding:utf-8
"""
@file: windows_information.py
@author: hjs
@ide: PyCharm
@createTime: 2021年06月07日  15点42分
@contactInformation: 727803257@qq.com
@Function: 请描述这个py文件的作用(范例：操作数据库来进行数据的存储更新)
"""

# 请从这行往下开始编写脚本

import wmi

c = wmi.WMI()


class Windows_information:
    """获取一台装有windows系统的电脑/笔记本的相关信息"""

    @staticmethod
    def system_information():
        """获取这台电脑安装的第一个windows操作系统的相关主要信息"""

        # 细节：
        # --》1.有可能一台电脑上装了很多个windows操作系统(大多数运营人员的电脑都只装一个windows操作系统)
        # --》2.我只需要拿第一个windows操作系统的相关主要信息来做相关判断的依据，没必要拿所有windows操作系统的
        # --》3.客户如果重装了不同版本的windows操作系统，从而导致权限校验失败的话，只能让客户重新找我们拿激活码进行激活

        # 获取到第一个windows操作系统的相关主要信息
        sysInformation = c.Win32_OperatingSystem()[0]
        # print(sysInformation)

        # 我主要拿值基本固定的字段来当判断的依据

        # 1.第一个字段: 操作系统的中文名(比如："Microsoft Windows 10 企业版")
        caption = sysInformation.Caption
        # print(caption)

        # 2.第二个字段: 操作系统的版本号(比如："10.0.18363")
        version = sysInformation.Version
        # print(version)

        # 3.第三个字段: 操作系统的版本号(比如："64 位")
        oSArchitecture = sysInformation.OSArchitecture
        # print(oSArchitecture)

        # 4.第四个字段: 操作系统的用于激活操作系统的产品ID(比如："00329-00000-00003-AA831")
        serialNumber = sysInformation.SerialNumber
        # print(serialNumber)

        data = {}
        data.update({"caption": caption})
        data.update({"version": version})
        data.update({"oSArchitecture": oSArchitecture})
        data.update({"serialNumber": serialNumber})
        # 返回包含这四个字段的数据，数据类型为dict
        return data

    @staticmethod
    def cpu_information():
        """获取这台电脑安装的第一个处理器(cpu)的相关主要信息"""

        # 细节：
        # --》1.有可能一台电脑上装了很多个处理器(大多数运营人员的电脑都只装一个处理器)
        # --》2.我只需要拿第一个处理器的相关主要信息来做相关判断的依据，没必要拿所有处理器的
        # --》3.客户如果重装了不同的处理器，从而导致权限校验失败的话，只能让客户重新找我们拿激活码进行激活

        # 获取到第一个处理器的相关主要信息
        cpuInformation = c.Win32_Processor()[0]
        # print(cpuInformation)

        # 我主要拿值基本固定的字段来当判断的依据

        # 1.第一个字段: 处理器的中文名(比如："Intel(R) Core(TM) i5-4460  CPU @ 3.20GHz")
        cpuName = cpuInformation.Name.strip()
        # print(cpuName)

        data = {}
        data.update({"cpuName": cpuName})

        # 返回包含这一个字段的数据，数据类型为dict
        return data

    @staticmethod
    def network_information():
        """获取这台电脑安装的第一个网络接口的相关主要信息"""

        # 细节：
        # --》1.有可能一台电脑上装了很多个网络接口(大多数运营人员的电脑都只开启一个网络接口)
        # --》2.我只需要拿第一个网络接口的相关主要信息来做相关判断的依据，没必要拿所有网络接口的
        # --》3.客户如果弄了不同的网络接口，从而导致权限校验失败的话，只能让客户重新找我们拿激活码进行激活

        # 获取到第一个网络接口的相关主要信息
        interface = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[0]
        # print(interface)

        # 我主要拿值基本固定的字段来当判断的依据

        # 1.第一个字段: 网络接口的mac地址(比如："40:8D:5C:D4:58:1F")
        macAddress = interface.MACAddress
        # print(macAddress)

        # 2.第二个字段: 网络接口的内网ipv4地址(比如："192.168.1.81")
        ipv4_address = interface.IPAddress[0]
        # print(ipv4_address)

        # 3.第三个字段: 网络接口的外网ipv6地址(比如："fe80::f827:18ae:5706:5d91")
        ipv6_address = interface.IPAddress[1]
        # print(ipv6_address)

        data = {}
        data.update({"macAddress": macAddress})
        data.update({"ipv4_address": ipv4_address})
        data.update({"ipv6_address": ipv6_address})
        # 返回包含这三个字段的数据，数据类型为dict
        return data

    @classmethod
    def information(cls):
        """获取一台装有windows系统的电脑/笔记本的相关信息"""
        first_data = cls.system_information()
        second_data = cls.cpu_information()
        third_data = cls.network_information()
        value = {}
        value.update(first_data)
        value.update(second_data)
        value.update(third_data)
        return value


if __name__ == '__main__':
    windows_information = Windows_information()
    information = windows_information.information()
    print(information)
    network = windows_information.network_information()
    print(network)
