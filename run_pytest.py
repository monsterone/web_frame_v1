

import pytest
if __name__ == '__main__':
    # command_line = ["-s", "./tests/test1/test1.py", "--alluredir=report"]
    command_line = ["-m","invest","--reruns","2","--reruns-delay","5","-s","--alluredir=Outputs/allure_reports"]
    pytest.main(command_line)



