import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from functions import get_values, send_message, send_message_to_chat
from init import get_users
from table_parser import mailing


def main():
    token, group_id, chat_id = get_values()
    admins_id = get_users()
    hi_message = 'Привет ✨\nЭто бот Посвящения в студенты 2023\nЗдесь ты будешь получать важную информацию о нашем мероприятии 🌱\nДо встречи на Жатве 🔥'
    try:
        vk_session = vk_api.VkApi(token=token)
        longpoll = VkBotLongPoll(vk_session, group_id)
    except Exception as ex:
        print('Ошибка', ex)
        exit(-1)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message['from_id']
            message = event.obj.message['text'].strip()
            if message:
                if message.lower() == 'начать' or message.lower() == 'привет':
                    send_message(user_id, hi_message)
                elif message[0] == '/':
                    try:
                        lst = message.split()
                        if lst[0] == '/send_message' and user_id in admins_id:
                            table = lst[1]
                            cell = lst[2]
                            value = lst[3]
                            m = ' '.join(lst[4:])
                            # print(m)
                            a = mailing(table, cell, value, m)
                            if type(a) == list:
                                send_message(user_id, 'Рассылка отправлена')
                                if a:
                                    response = ''
                                    for i in a:
                                        response += i+'\n'
                                    send_message(user_id, f'По каким то причинам не доставлена(скорее всего, не зашли в бота): {response}')
                            else:
                                send_message(user_id, 'Ошибка рассылки')

                    except Exception as ex:
                        send_message(user_id, 'Ошибка рассылки')
                        print(ex)
                else:
                    # отправить сообщение в беседу
                    send_message_to_chat(message, user_id)


if __name__ == '__main__':
    main()
