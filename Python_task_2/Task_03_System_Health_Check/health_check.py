import json


def process_server_data(json_string):
    try:
        data = json.loads(json_string)
        servers = data.get("servers", [])
        for server in servers:
            name = server.get("name", "Unknown")
            status = server.get("status", "Unknown")
            if status == "up":
                status_icon = "Success"
            else:
                status_icon = "Failed"
            print(f"{status_icon} {name}: {status}")
    except json.JSONDecodeError as e:
        print("ERROR: Invalid JSON format!")
        print(f"Details: {e}")


if __name__ == "__main__":
    mock_api = (
        '{"servers": [{"name": "web-01", "status": "up"}, '
        '{"name": "db-01", "status": "down"}]}'
    )
    process_server_data(mock_api)
