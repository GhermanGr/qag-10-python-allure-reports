import allure
from selene import browser, by, be
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "grebeniukg")
@allure.feature("Repository UI")
@allure.story("Issues tab should be present on repository screen.")
@allure.link("https://github.com", name="Testing")
def test_github_decorators():
    repo_link = 'GhermanGr/qaguru-pb-hw-5'
    open_github()
    search_repository(repo_link)
    go_repository(repo_link)
    check_issues()

@allure.step('Open the github main page')
def open_github():
    browser.open('https://github.com')

@allure.step('Search for repository')
def search_repository(repo_link):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo_link).press_enter()

@allure.step('Go to repository')
def go_repository(repo_link):
    browser.element(by.link_text(repo_link)).click()

@allure.step('Check for Issues tab')
def check_issues():
    browser.element('#issues-tab').should(be.visible)