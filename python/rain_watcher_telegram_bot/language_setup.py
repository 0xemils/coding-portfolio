def set_language(lang: str):
    global welcome_message, change_language_button_text, continue_text, city_setup_message, time_setup_message, confirmation_message, \
        setup_message, finnish_lang_button_text, chinese_lang_button_text, english_lang_button_text, unsubscribe_message, rain_message, \
        incorrect_input, incorrect_input_setup_message, city_not_found

    if lang == "fi":
        welcome_message = '''Hei %s! 👋

Olen *Rain Watcher Bot* - Tarkistan sään seuraavat 12 tuntia joka päivä valitsemaasi aikaan ja ilmoitan, jos sataa ⛈

*Aloita painamalla alla olevaa Jatka-painiketta!*'''
        change_language_button_text = "Vaihda kieli 🌐"

        continue_text = "Jatkaa ➡️"

        city_setup_message = "Mikä on sen kaupungin nimi, josta haluat minun tarkistavan sään? 📍"
        time_setup_message = '''Hyvä on! ✅ *Mihin aikaan haluat minun lähettävän ilmoituksia?*
        
Käytä seuraavaa ajan muotoa: hh:mm'''
        confirmation_message = "Valmis! Tarkistan joka päivä osoitteessa %s ja ilmoitan, jos %s sataa ☔️"

        setup_message = "Valitse jokin alla olevista kielistä:"
        finnish_lang_button_text = "Suomi 🇫🇮 (Nykyinen)"
        chinese_lang_button_text = "Kiina 🇨🇳"
        english_lang_button_text = "Englanti 🇺🇸"

        incorrect_input = "⚠️ Syöte on väärä, yritä uudelleen!"
        incorrect_input_setup_message = "Syöte on virheellinen ⚠️ Käytä /setup komentoa, jos haluat muuttaa botin asetuksia."
        city_not_found = "Kaupunkia ei löydy, yritä uudelleen"

        unsubscribe_message = "Olet onnistuneesti peruuttanut bottiviestien tilauksen! Et saa enää ilmoituksia 🔕"

        rain_message = '''Hei siellä! 🌧️

Tänään %s kaupungissa on odotettavissa sadetta.
Älä jää kiinni ilman sateenvarjoa tai sadetakkia! ☔️

Pysy kuivana ja mukavaa päivää!


Kippis,
Sateen tarkkailija'''

    elif lang == "zh_cn":
        welcome_message = '''嗨%s！ 👋

我是*Rain Watcher Bot* - 我会每天在您指定的时间查看未来 12 小时的天气，并通知您是否会下雨 ⛈

*要开始，请按下面的继续按钮！*'''
        change_language_button_text = "更改语言 🌐"

        continue_text = "继续 ➡️"

        city_setup_message = "您想让我查看天气的城市叫什么名字？ 请提供城市的英文名称📍"
        time_setup_message = '''好吧！✅ *您希望我什么时候发送通知？*
        
请使用以下时间格式：hh:mm'''
        confirmation_message = "可以了，好了！ 我会每天在 %s 查看并通知您 %s 是否会下雨☔️"

        setup_message = "请从以下语言中选择一种："
        finnish_lang_button_text = "芬兰语🇫🇮"
        chinese_lang_button_text = "中文🇨🇳（当前）"
        english_lang_button_text = "英语🇺🇸󠁢󠁥󠁮󠁧󠁿"

        incorrect_input = "⚠️输入错误，请重试！"
        incorrect_input_setup_message = "输入无效⚠️如果您想更改机器人的设置，请使用 /setup 命令。"
        city_not_found = "找不到城市，请重试"

        unsubscribe_message = "你已成功取消订阅！ 您将不会再收到通知🔕"

        rain_message = '''嘿！ 🌧️

预计今天 %s 有雨。
没有雨伞或雨衣，不要被抓住！ ☔️

保持干燥，度过美好的一天！


干杯，
Rain Watcher'''

    else:
        welcome_message = '''Hi %s! 👋

I'm a *Rain Watcher Bot* - I'll check the weather for the next 12 hours every day at your specified time and notify you if it's going to rain ⛈

*To get started please press the continue button below!*'''
        change_language_button_text = "Change Language 🌐"

        continue_text = "CONTINUE ➡️"

        city_setup_message = "What is the name of the city you want me to check the weather for? 📍"
        time_setup_message = '''Alright! ✅ *At what time do you want me to send notifications?*
        
Please use the 24-hour time format: hh:mm'''
        confirmation_message = "All set! I'll be checking every day at %s and notify you if it's going to rain in %s ☔️"

        setup_message = "Please choose from one of the languages below:"
        finnish_lang_button_text = "Finnish 🇫🇮"
        chinese_lang_button_text = "Chinese 🇨🇳"
        english_lang_button_text = "English 🇺🇸󠁧 (Current)󠁢󠁥󠁮󠁧󠁿"

        incorrect_input = "⚠️ The input is incorrect, please try again!"
        incorrect_input_setup_message = "The input is invalid ⚠️ Please use the /setup command if you wish to change the bot's settings."
        city_not_found = "The city cannot be found, please try again"

        unsubscribe_message = "You have successfully unsubscribed! You won't get notifications anymore 🔕"

        rain_message = '''Hey there! 🌧️

There's rain expected in %s today. 
Don't get caught without an umbrella or raincoat! ☔️

Stay dry and have an awesome day!


Cheers,
Rain Watcher'''
