# b4uleave Plugin

## Overview

The B4ULeave plugin displays a modal window asking the user whether they want to leave the page when the beforeunload event occurs.

## Installation

```sh
pip install platzky-b4uleave
```

## Usage

```json
"plugins": [
    {
        "name": "b4uleave",
        "config": {
            "message": "Your custom message goes here"
        }
    }
]
```

If you omit `message`, it defaults to:

```html
<p>'Czy na pewno chcesz<br>opuścić naszą stronę?'</p>
```