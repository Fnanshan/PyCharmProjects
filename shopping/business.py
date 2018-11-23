class user(object):

    def __init__(self, username='daemon', userpass='daemon', userbalance=10000):
        self.username = username
        self.userpass = userpass
        self.userbalance = userbalance

    def get_userbalance(self):
        return self.userbalance


plist = [('MacPro',9000),
         ('Python',1020),
         ('Tesla',900000),
         ('bikes',3000),
         ('kandle',4000)]
while True:
    userD = user()
    username = str(input('please input username str :'))
    userpass = str(input('please input userpass str :'))
    if username != userD.username and userpass != userD.userpass:
        print('username or userpass error！，please re-Enter :')
    else:
        print('----------------------------------------------------------------------------------')
        print('You balance is %s' % userD.get_userbalance())
        print('Product catalogue :')
        print(list(plist))
        print('-----------------------------------------------------------------------------------')
        pname = str(input('Please enter the name of the item you purchased :'))
        for n in list(plist):
            if n[0] == pname:
                if n[1] <= userD.get_userbalance():
                    judge = int(input('Can be purchased, please enter 1 to confirm the purchase :'))
                    if judge:
                        userD.userbalance = userD.get_userbalance() - n[1]
                        print('The balance is still %s' % userD.get_userbalance())
                    else:
                        print('Thank you for coming, welcome to come back next time.')
                        break
                else:
                    print('I do not have enough money')
                    break
            else:
                # print('No such item，enter 1 continue purchase ')
                continue


