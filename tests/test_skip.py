"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture()
def browser_management():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://github.com')
    yield


def test_github_desktop(browser_management):
    if browser.config.window_width <= 1000:
        pytest.skip(reason='Mobile window size')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_management):
    if browser.config.window_width > 1000:
        pytest.skip(reason='Desktop window size')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))