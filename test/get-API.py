from wsgiref import headers

from urllib3.util import request


def test_api_get(playwright):
    request = playwright.request.new_context()
    #     extraHTTPHeaders={
    #         "Accept": "application/json",
    #         "Authorization": "Bearer Your_Access_Token",
    #         "Content-Type": "application/json",
    #         "X-API-Key": "Your_API_Key"
    #
    #     }
    #
    # )
    response = request.get("https://jsonplaceholder.typicode.com/posts/1",
                           headers={"Accept": "application/json"})
    assert response.status == 200
    json_data = response.json()
    print("=============TEST==============")
    print(json_data)
    assert json_data["id"] == 1
    title = json_data["title"]
    print("Title is "+title)

    request.dispose()
    print("Test Completed")