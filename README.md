# B4ULeave Plugin

## Overview

Plugin B4ULeave wyświetla modalne okno z pytaniem, czy użytkownik chce opuścić stronę przy zdarzeniu `beforeunload`.

## Installation

```sh
pip install platzky-B4ULeave
```

## Usage

```json
"plugins": [
    {
        "name": "B4ULeave",
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