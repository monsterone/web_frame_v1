



# 正常用例 -投资成功
inverst_success = {"money":100,"check":100.0,"msg":"正常投资-成功"}


# 异常用例 - 弹框提示(还有很多用例，为了运行时间，目前写几个案例)
inverst_fail_alert = [
    {"money":10,"check":"投标金额必须为100的倍数","msg":"异常投资-失败"},
    {"money":0,"check":"请正确填写投标金额","msg":"异常投资-失败"}
]

# 异常用例 - 按钮提示
inverst_fail_button = [
    {"money":66,"check":"请输入10的整数倍","msg":"异常投资-失败"},
    {"money":"abc","check":"请输入10的整数倍","msg":"异常投资-失败"}
]
