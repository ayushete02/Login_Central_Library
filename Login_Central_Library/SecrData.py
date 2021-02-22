
def Email_sec_Data_by_Reg_btn():


    File = open('Data/MData.txt')
    Mess = File.read()
    File.close()
    import smtplib
    from plyer import notification

    GI = 'centrallibraryproject@gmail.com'
    O = 'centrallibraryproject@gmail.com'
    GPWD = 'Password_Library_123456789'
    Course = 'Central Library verification code'

    try:

        Email = smtplib.SMTP('smtp.gmail.com', 587)
        Email.starttls()
        Email.login(GI, GPWD)
        Email.sendmail(
            GI, O, f"Course: {Course}\n\n{Mess}")
        
        ICON_PATH = "Icons\\Logo.ico"
        notification.notify(
            app_icon = ICON_PATH,
            title="Central Library",
            message=f"Your Email is Registered\nyou can now Login\nusing your id/password",
       
            timeout=4
        )
        print("Sent")
        Email.Exit_TK()
    except:
        pass


#O O
# saf3q4egvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtgvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeahtedhth gvrqe45khlb,tyh5bgtuhy54juh64wjrtjr6w5jwj4 sxbgarhetazdfntgfntrg tbnhdtrahndtg athrtedah rthtdeaht GID%%centrallibraryproject@gmail.com GMPWD%%Password_Library_123456789