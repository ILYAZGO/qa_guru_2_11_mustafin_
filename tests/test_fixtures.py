"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support.shared import browser
from selene import have



@pytest.fixture()
def desktop_management():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://github.com')
    yield


@pytest.fixture()
def mobile_management():
    browser.config.window_width = 640
    browser.config.window_height = 960
    browser.open('https://github.com')
    yield


def test_github_desktop(desktop_management):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile_management):
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))