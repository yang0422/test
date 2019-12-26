__author__ = 'xuan'
import configparser


class ReadConfig:
    def read_config(self, file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='UTF-8')
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    value = ReadConfig().read_config('../Conf/url.Conf', 'HTTP', 'tenantId')
    print(value)
