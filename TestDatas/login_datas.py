

# 正常场景 - 测试数据
success_data = {"user":"18684720553","passwd":"python"}

# 异常用例 - 手机号格式不正确（大于11位、小于11位、为空、不在号码段）
phone_data = [
    {"user":"18684720","passwd":"python","check":"请输入正确的手机号"},
    {"user": "18684720553123", "passwd": "python", "check": "请输入正确的手机号"},
    {"user": "11684720553", "passwd": "python", "check": "请输入正确的手机号"},
    {"user": "", "passwd": "python", "check": "请输入手机号"},
    {"user":"18684720553","passwd":"","check":"请输入密码"}
]

# 异常用例 - 账号未注册，密码错误（中间提示）
phone_data_err = [
    {"user":"18088888888","passwd":"python","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"python666","check":"帐号或密码错误!"}
]
