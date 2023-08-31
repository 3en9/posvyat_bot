import vk_api
from init import get_values

token, group_id, chat_id = get_values()


def send_message(user_id, message):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        vk.messages.send(user_id=user_id, message=message, random_id=0)
        return 1
    except vk_api.ApiError:
        return 0
    except Exception as ex:
        print(f'Ошибка на вызов функции send_message для ({user_id} ; {message})', ex, sep='\n')
        return 0


def send_message_to_chat(message, user_id):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        name = get_name(user_id)
        if name:
            vk.messages.send(peer_id=chat_id, message=message + '\nСообщение от:' + name, random_id=0)
        else:
            vk.messages.send(peer_id=chat_id,
                             message='Что-то случилось... Проверьте сообщения сообщества вручную', random_id=0)
    except Exception as ex:
        print(f'Ошибка на вызов функции для send_message_to_chat ({message} ; {user_id})', ex, sep='\n')


def get_name(user_id):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        name = vk.users.get(user_ids=user_id)[0]
        return f'{name["first_name"]} {name["last_name"]}\nvk.com/id{user_id}'
    except Exception as ex:
        print(f'Ошибка на вызов функции get_name для ({user_id})', ex, sep='\n')
        return ''


def get_user_id(name):
    try:
        vk_session = vk_api.VkApi(token=token)
        user_id = vk_session.method('utils.resolveScreenName', {'screen_name': name})['object_id']
        return user_id
    except Exception as ex:
        print(f'Ошибка на вызов функции get_user_id для ({name})', ex, sep='\n')
        return ''


def main():
    # send_message(173587517, '123<br>')
    # print(get_name(65363464644636634643))
    print(get_user_id('3en9cs'))


if __name__ == '__main__':
    main()
