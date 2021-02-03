card_list = [];


def show_menu():
    """显示欢迎界面"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 v1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    # 1. 提示用户输入用户信息
    i_name = input("请输入姓名：")
    i_phone = input("请输入电话：")
    i_qq = input("请输入QQ：")
    email = input("请输入邮箱：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": i_name,
        "phone": i_phone,
        "i_qq": i_qq,
        "email": email
    }

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)

    # 4.提示用户添加成功
    print("添加【%s】的名片成功" % i_name)


def show_all():
    # 如果列表为空不显示表头
    if len(card_list) == 0:
        print("列表中还没有名片，请新增名片!!")
        return

    """显示所有名片"""
    print("-" * 50)
    # 打印表头
    print_headers()

    # 遍历名片字典，一次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["name"],
            card_dict["phone"],
            card_dict["i_qq"],
            card_dict["email"]
        ), end="\t\t")
    print("")


def search_card():
    """搜索名片"""
    print("-" * 50)
    find_name = input("请输入姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了 %s 的名片了：" % find_name)
            print_headers()
            print("%s\t\t%s\t\t%s\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["i_qq"],
                card_dict["email"]
            ), end="\t\t")
            print("")

            #  针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("没有找到 %s 的名片" % find_name)


def print_headers():
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)


def deal_card(find_dict):
    """处理查找到的名片

    @param find_dict:   查找到的名片
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作："
                       "【1】 修改 【2】 删除 【0】 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "phone：")
        find_dict["i_qq"] = input_card_info(find_dict["i_qq"], "i_qq：")
        find_dict["email"] = input_card_info(find_dict["email"], "email：")

        print("名片修改成功！")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("删除名片成功!")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    @param dict_value:  字典中原有的值
    @param tip_message: 输入的提示文字
    @return:    如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1. 提示用户输入信息
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3. 如果用户没有输入内容，返回`字典中原有的值`。
    else:
        return dict_value
