import gspread
from functions import get_user_id, send_message
table_name = 'posvyat-test'
json_file = 'table.json'

reg_message = 'Поздравляю! \nТы успешно прошел(а) регистрацию на самое незабываемое событие студенчества 🎯'
transfer_message = 'В дорогу 🚌\nТы успешно прошел(а) регистрацию на трансфер.'
living_message = 'Выспаться сможешь 🛌 \nТы зарегистрировался(ась). На Посвяте хорошо отдохнешь после захватывающей программы.'


def main():
    gc = gspread.service_account(filename=json_file)
    sh = gc.open(table_name)
    worksheet = sh.worksheet('registration')
    print(worksheet.get_all_records())
    worksheet = sh.worksheet('transfer')
    print(worksheet.get_all_records())
    worksheet = sh.worksheet('resettlement')
    print(worksheet.get_all_records())


def mailing(table, row, value, m):
    """
    table - нужный лист, row - нужное поле, value - значение, m - сообщение
    value для любого значения (any_value)
    """
    pass
    if table and row and value and m:
        warn = []  # пользователи, которым сообщение не дошло
        try:
            gc = gspread.service_account(filename=json_file)
            sh = gc.open(table_name)
            worksheet = sh.worksheet(table)
            a = worksheet.get_all_records()
        except Exception as ex:
            print(f'Ошибка на вызов функции mailing для ({table} ; {row} ; {value} : {m})', ex, sep='\n')
            return -1
        for cell in a:
            if value == str(cell[row]) or value == 'any_value':
                user = cell['vkurl'].split('/')[-1]
                if user[:2] == 'id':
                    user = user[2:]
                else:
                    user = get_user_id(user)
                if user:
                    tmp = send_message(user, m)
                    if not tmp:
                        warn.append(cell['vkurl'])
                else:
                    warn.append(cell['vkurl'])
        if len(warn) == len(a):
            return -1
        return warn
    return -1


def check_registration():
    try:
        gc = gspread.service_account(filename=json_file)
        sh = gc.open(table_name)
        worksheet = sh.worksheet('registration')
        with open('registration_list.txt') as file:
            current = []
            for i in file.readlines():
                if i:
                    current.append(int(i.replace('\n', '')))
        file.close()

        a = worksheet.get_all_records()
        for row in a:
            user = row['vkurl'].split('/')[-1]
            if user[:2] == 'id':
                user = user[2:]
            else:
                user = get_user_id(user)
            if user not in current and user != '':
                tmp = send_message(user, reg_message)
                if tmp:
                    with open('registration_list.txt', 'a') as file:
                        file.writelines(str(user))
    except Exception as ex:
        print(f'Ошибка на вызов функции check_registration', ex, sep='\n')


def check_transfer():
    try:
        gc = gspread.service_account(filename=json_file)
        sh = gc.open(table_name)
        worksheet = sh.worksheet('transfer')
        with open('transfer_list.txt') as file:
            current = []
            for i in file.readlines():
                if i:
                    current.append(int(i.replace('\n', '')))
        file.close()

        a = worksheet.get_all_records()
        for row in a:
            user = row['vkurl'].split('/')[-1]
            if user[:2] == 'id':
                user = user[2:]
            else:
                user = get_user_id(user)
            if user not in current and user != '':
                tmp = send_message(user, transfer_message)
                if tmp:
                    with open('transfer_list.txt', 'a') as file:
                        file.writelines(str(user))
    except Exception as ex:
        print(f'Ошибка на вызов функции check_transfer', ex, sep='\n')


def check_living():
    try:
        gc = gspread.service_account(filename=json_file)
        sh = gc.open(table_name)
        worksheet = sh.worksheet('living')
        with open('living_list.txt') as file:
            current = []
            for i in file.readlines():
                if i:
                    current.append(int(i.replace('\n', '')))
        file.close()

        a = worksheet.get_all_records()
        for row in a:
            user = row['vkurl'].split('/')[-1]
            if user[:2] == 'id':
                user = user[2:]
            else:
                user = get_user_id(user)
            if user not in current and user != '':
                tmp = send_message(user, living_message)
                if tmp:
                    with open('living_list.txt', 'a') as file:
                        file.writelines(str(user))
    except Exception as ex:
        print(f'Ошибка на вызов функции check_living', ex, sep='\n')


if __name__ == '__main__':
    # main()
    check_registration()
    check_transfer()
    check_living()
