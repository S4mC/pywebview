"""pywebview custom events example"""

import webview

def on_custom_event_1(e=None, Text=None):
    print(f"Python event 1 triggered from JS, data: {e['dataText']}, Text: {Text}")
    return False # Returning False is like e.preventDefault() was called in window.dispatch_custom_event

def on_custom_event_2(e=None, Text=None):
    print(f"Python event 2 triggered from JS, data: {e['dataText']}, Text: {Text}")


if __name__ == '__main__':
    window = webview.create_window(
        'JavaScript to Python Events',
        html="""<html><body>

            // This button calls custom_event_1 in python
            <button onclick="pywebview.dispatch_custom_event('custom_event_1', { 'dataText': 'Content' }, 'optional additional parameter').then(result => log('Result: ' + JSON.stringify(result)));">custom_event_1</button>

            // This button calls custom_event_2 in python
            <button onclick="pywebview.dispatch_custom_event('custom_event_2', { 'dataText': 'Content' }, 'optional additional parameter').then(result => log('Result: ' + JSON.stringify(result)));">custom_event_2</button>

            <div id="output" style="min-height: 100px;"></div>
            
            <script>
                function log(message){ document.getElementById('output').innerHTML += message + '<br>'; };
            </script>
        </body></html>"""
    )
    
    window.events.custom_event_1 += on_custom_event_1
    window.events.custom_event_2 += on_custom_event_2

    webview.start()