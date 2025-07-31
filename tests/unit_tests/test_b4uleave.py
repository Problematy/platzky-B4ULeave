from typing import Any, Dict
from platzky.platzky import create_app_from_config, Config


def test_that_plugin_loads_b4uleave():

    data_with_plugin: Dict[str, Any] = {
            "APP_NAME": "testingApp",
            "SECRET_KEY": "secret",
            "USE_WWW": False,
            "BLOG_PREFIX": "/",
            "TRANSLATION_DIRECTORIES": ["/some/fake/dir"],
            "DB": {
                "TYPE": "json",
                "DATA": {
                    "site_content": {"pages": []},
                    "plugins": [{
                        "name": "b4uleave",
                        "config": {
                            "message": "Your custom message goes here",
                            "stay": "Staying custom message",
                            "leave": "Leaving custom message"
                        }
                    }]
                },
            },
    }

    # expected data
    b4uleave_function = "B4ULeave-ModalWindow"
    custom_message = "Your custom message goes here"
    custom_stay = "Staying custom message"
    custom_leave = "Leaving custom message"

    config_with_plugin = Config.model_validate(data_with_plugin)

    app_with_plugin = create_app_from_config(config_with_plugin)

    response = app_with_plugin.test_client().get("/")

    assert response.status_code == 404
    decoded_response = response.data.decode()
    assert b4uleave_function in decoded_response
    assert custom_message in decoded_response
    assert custom_stay in decoded_response
    assert custom_leave in decoded_response

    assert '<div class="B4ULeave-Content"' in decoded_response
    assert "<p>Your custom message goes here</p>" in decoded_response
    assert "Staying custom message" in decoded_response
    assert "Leaving custom message" in decoded_response
