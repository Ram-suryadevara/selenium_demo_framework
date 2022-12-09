import configparser
# Creating object
config = configparser.RawConfigParser()  # Class
config.read('.\\configurations\\config.ini')


class ReadConfig:
    """
    Details from the config.ini file. for every variable, creating a new method.
    """
    @staticmethod  # without creating object,calling using classname.
    def get_applicationurl():
        """
        method to get the URL link
        :return: URL
        """
        # ('1st argument'-info, 'property value')
        url = config.get('login_info', 'base_URL')
        return url

    @staticmethod
    def get_useremail():
        """
        method to get the username.
        :return: username
        """
        username = config.get('login_info', 'useremail')
        return username

    @staticmethod
    def get_password():
        """
        method to get the password during login
        :return: password
        """
        password = config.get('login_info', 'password')
        return password
