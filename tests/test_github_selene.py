import allure
from selene import browser, by, be
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "grebeniukg")
@allure.feature("Repository UI")
@allure.story("Issues tab should be present on repository screen.")
@allure.link("https://github.com", name="Testing")
def test_github_selene():
    browser.open('https://github.com')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('GhermanGr/qaguru-pb-hw-5').press_enter()

    browser.element(by.link_text('GhermanGr/qaguru-pb-hw-5')).click()

    browser.element('#issues-tab').should(be.visible)