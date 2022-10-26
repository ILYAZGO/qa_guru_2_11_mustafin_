"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import have
from selene.support.shared import browser

mobile_width = 640
mobile_height = 960
desktop_width = 1280
desktop_height = 720


@pytest.fixture(params=[(desktop_width, desktop_height)])
def browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com')
    yield


def test_github_desktop(browser_management):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize(
    'browser_management',
    [(mobile_width, mobile_height)],
    indirect=True,
    ids=['Switch to mobile window size'],
)
def test_github_mobile(browser_management):
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))