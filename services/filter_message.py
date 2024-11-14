def filtered_hostage_word(message_data):
    keywords = ['hostage']
    message_text = str(message_data).lower()
    return any(keyword in message_text for keyword in keywords)


def filtered_explosive_word(message_data):
    keywords = ['explosive']
    message_text = str(message_data).lower()
    return any(keyword in message_text for keyword in keywords)