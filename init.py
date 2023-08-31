import os
from dotenv import load_dotenv, find_dotenv


def get_values():
    load_dotenv(find_dotenv())
    token = os.environ.get('token')
    group_id = os.environ.get('group_id')
    chat_id = os.environ.get('chat_id')
    return token, group_id, chat_id


def get_users():
    with open('admin_ids.txt') as file:
        users = file.read().split('\n')
    return list(map(int, users))


def main():
    print(get_values())
    print(get_users())


if __name__ == '__main__':
    main()
