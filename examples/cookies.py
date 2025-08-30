"""A cookies and local storage example."""

import webview


def read_cookies(window):
    cookies = window.get_cookies()
    for c in cookies:
        print(c.output())


class Api:
    def clearCookies(self):
        window.clear_cookies()

if __name__ == '__main__':
    window = webview.create_window('Cookie example', 'assets/cookies.html', js_api=Api())

    # We need to explicitly set a http port to persist cookies between sessions
    webview.start(read_cookies, window, private_mode=False, http_server=True, http_port=13377)
