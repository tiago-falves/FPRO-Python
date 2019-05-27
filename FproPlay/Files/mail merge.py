def mail_merge(names, mail_template):
    l=[]
    with open(names,"r") as file_name, open(mail_template,"r") as file_mail:
        mail=file_mail.read()
        for name in file_name.readlines():
            a=mail.replace("<name>",name.strip())

            l.append(a)
    return l
        
