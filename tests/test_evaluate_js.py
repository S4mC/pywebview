import pytest

import webview

from .util import run_test


@pytest.fixture
def window():
    return webview.create_window(
        'Evaluate JS test', html='<html><body><div id="node">TEST</div></body></html>'
    )


def test_mixed(window):
    run_test(webview, window, mixed_test)


def test_array(window):
    run_test(webview, window, array_test)


def test_object(window):
    run_test(webview, window, object_test)


def test_string(window):
    run_test(webview, window, string_test)


def test_int(window):
    run_test(webview, window, int_test)


def test_float(window):
    run_test(webview, window, float_test)


def test_undefined(window):
    run_test(webview, window, undefined_test)


def test_null(window):
    run_test(webview, window, null_test)


def test_nan(window):
    run_test(webview, window, nan_test)


def test_body(window):
    run_test(webview, window, body_test)


def test_document(window):
    run_test(webview, window, document_test)


def test_node(window):
    run_test(webview, window, node_test)


def test_exception(window):
    run_test(webview, window, exception_test)


def mixed_test(window):
    result = window.evaluate_js(
        """
        document.body.style.backgroundColor = '#212121';
        // comment
        function test() {
            return 2 + 2;
        }
        test();
    """
    )
    assert result == 4


def array_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return [undefined, 1, 'two', 3.00001, {four: true}]
    }
    getValue()
    """
    )
    assert result == [None, 1, 'two', 3.00001, {'four': True}]


def object_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return {1: 2, 'test': true, obj: {2: false, 3: 3.1}}
    }

    getValue()
    """
    )
    assert result == {'1': 2, 'test': True, 'obj': {'2': False, '3': 3.1}}


def string_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return "this is only a test"
    }

    getValue()
    """
    )
    assert result == 'this is only a test'


def int_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return 23
    }

    getValue()
    """
    )
    assert result == 23


def float_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return 23.23443
    }

    getValue()
    """
    )
    assert result == 23.23443


def undefined_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return undefined
    }

    getValue()
    """
    )
    assert result is None


def null_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return null
    }

    getValue()
    """
    )
    assert result is None


def nan_test(window):
    result = window.evaluate_js(
        """
    function getValue() {
        return NaN
    }

    getValue()
    """
    )
    assert result is None


def body_test(window):
    result = window.evaluate_js('document.body')

    assert result['nodeName'] == 'BODY'


def document_test(window):
    result = window.evaluate_js('document')

    assert result['nodeName'] == '#document'


def node_test(window):
    node = window.evaluate_js('document.querySelector("#node")')

    assert node['id'] == 'node'
    assert node['innerText'] == 'TEST'


def exception_test(window):
    with pytest.raises(webview.errors.JavascriptException):
        window.evaluate_js('eklmn')
