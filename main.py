import extensions


def main():
    ## Временно
    vk_session = extensions.VkApi(login=input(), password=input())
    vk_session.auth()
    vk = vk_session.get_api()
    vk.wall.post('VkApi work.')


if __name__ == '__main__':
    main()
