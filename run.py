from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.select_place_to_go(input("Ban muon di dau ?"))
        bot.select_dates(check_in_date=input("Ngay muon phong ?"),
                         check_out_date=input("Ngay tra phong ?"))
        bot.select_adults(int(input("Co bao nhieu ngươi ?")))
        bot.click_search()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise