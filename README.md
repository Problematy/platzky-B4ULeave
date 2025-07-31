# b4uLeave Plugin

## Overview

The B4ULeave plugin displays a modal window asking the user whether they want to leave the page when the beforeunload event occurs.

## Installation

```sh
pip install platzky-b4uLeave
```

## Usage

```json
"plugins": [
    {
        "name": "b4uLeave",
        "config": {
            "message": "Your custom message goes here",
            "stay": "Staying custom message",
            "leave": "Leaving custom message"
        }
    }
]
```

If you omit `message`, it defaults to:

```html
<p>'Are you sure you want<br>to leave our page?'</p>
```

If you omit `stay`, it defaults to:

```html
<p>'Stay'</p>
```

If you omit `leave`, it defaults to:

```html
<p>'Leave'</p>
```