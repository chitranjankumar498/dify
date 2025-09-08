import requests
import json
def main(url:str,name:str ) -> dict:
    # Step 1: Get file info from Start Node
    #file_info = inputs["file"]
    #file_url = file_info["url"]
    #file_name = file_info["name"]

    # Step 2: Download the file
    #file_content = requests.get(file_url).content
    file_content = requests.get(url).content

    # Step 3: API details
    url = "http://host.docker.internal/v1/datasets/838b5050-8dc6-4967-9a8a-bc181c9156b5/document/create-by-file"
    headers = {
        "Authorization": "Bearer dataset-REGgvHt3LTfDsnjT2JwVWOLk"
    }

    # Step 4: Metadata
    data = {
        "data": """{
            "indexing_technique": "high_quality",
            "process_rule": {
                "rules": {
                    "pre_processing_rules": [
                        {"id": "remove_extra_spaces", "enabled": true},
                        {"id": "remove_urls_emails", "enabled": true}
                    ],
                    "segmentation": {"separator": "###", "max_tokens": 500}
                },
                "mode": "custom"
            },
            "data_source_type": "upload_file"
        }"""
    }

    # Step 5: File payload
    files = {
        "file": (name, file_content, "application/octet-stream")
    }

    # Step 6: Send request
    response = requests.post(url, headers=headers, data=data, files=files)

    # Step 7: Return response
    try:
        return {"status": str(response.status_code), "result": response.text}
    except Exception:
        return {"status": str(response.status_code), "result": response.text}
