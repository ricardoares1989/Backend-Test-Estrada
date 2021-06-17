import urllib3

http = urllib3.PoolManager()


def slack_notifier(slack_message: str, destiny: str) -> int:
    """
    Args:
        slack_template (str)): Enter a JSON string
        destiny (str): Url path to channel.
    Returns:
        status_code (int)
    """

    request = http.request(
        "POST",
        destiny,
        body=slack_message,
        headers={"Content-type": "application/json"},
    )
    return request.status
