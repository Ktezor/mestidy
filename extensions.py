import vk_api as __vk_api
import exceptions


def save_captcha(captcha, filename='captcha.jpg'):
    if '/' in filename | '\\' in filename:
        raise exceptions.MestidyApiError('Неверно задано имя файла. Пожалуйста, не указывайте директорию к файлу.')
    with open(filename, 'wb') as file:
        file.write(captcha.get_image())
    pass


class VkApi(__vk_api.VkApi):

    def __init__(self, login, password, token=None, auth_handler=None, captcha_handler=None, app_id=6222115):

        super().__init__(login=login, password=password, token=token, auth_handler=auth_handler,
                         captcha_handler=captcha_handler, app_id=app_id)
        self.config = {
            'remember_2fa': True
        }

    def auth_handler(self):
        print('Двухфакторная авторизация. Пожалуйста, введите ваш код: ')
        return input('Код:'), self.config['remember_2fa']

    def captcha_handler(self, captcha):

        print('Сохраняю капчу в корневую директорию проекта.')
        save_captcha(captcha)
        return captcha.try_again(input('Пожалуйста, введите капчу: '))
