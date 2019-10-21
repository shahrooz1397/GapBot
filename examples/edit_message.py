from gapbot import Gap  # import library;

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;

if __name__ == '__main__':  # If you are running this module as the main program;
    target_id = 000000  # whose to be send text to him;
    text = "GapBot SendText"
    new_text = 'GapBot SendEditedText'
    msg = app.send_text(
        chat_id=target_id,  # https://developer.gap.im/doc/botplatform#chatId-description
        text=text,
    )
    app.edit_message(
        chat_id=target_id,
        message_id=msg.json()['id'],
        new_text=new_text,
    )

# https://developer.gap.im/doc/botplatform#method-edit-message
