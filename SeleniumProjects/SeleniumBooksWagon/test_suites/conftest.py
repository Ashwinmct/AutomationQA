import pytest
from selenium import webdriver

from object_repository import constants


@pytest.yield_fixture()
def get_driver_object():
    global driver
    driver = webdriver.Chrome(executable_path=constants.CHROME_DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()


def __capture_screenshot(screen_shot_file_name):
    driver.get_screenshot_as_file(screen_shot_file_name)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            __capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"onclick="window.open(' \
                       'this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra
