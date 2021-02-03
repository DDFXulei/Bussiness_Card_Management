import card_tools


while True:
    # TODO 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是 【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1","2","3"]:
        #新增名片
        if action_str == "1":
            card_tools.new_card()
        #显示全部
        elif action_str == "2":
            card_tools.show_all()
        #查询名片
        elif action_str == "3":
            card_tools.search_card()

    #0 退出系统
    elif action_str == '0':
        #pass 关键字表示一个占位符
        print("欢迎再次使用【名片管理系统】")
        break
        # pass
    #其他输入操作，需要重新出错
    else:
        print("您输入的不正确，请重新输入!")