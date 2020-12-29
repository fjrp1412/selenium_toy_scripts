from message_ig import InstagramMessage
def option_list():

    option = int(input(
        f'1: send message\n'
        f'2: create new account\n'
    ))
    return option

def options(option,account, password):
    if(option == 1):
        message_instagram = InstagramMessage(account, password)
        message_instagram.sendMessage()
    else:
        print("Option not found")



if __name__ == "__main__":
    option_list()
