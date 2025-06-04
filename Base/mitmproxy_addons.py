from mitmproxy import http
import os
import json
from datetime import datetime


class SaveXHRRequests:
    def __init__(self):
        self.base_log_dir = "/mnt/k/automation/Automation_scripts/mitmproxy_logs"  # Root log folder

    def response(self, flow: http.HTTPFlow):
        # Filter only XHR/JSON requests
        content_type = flow.response.headers.get("content-type", "")
        if "application/json" in content_type or "xhr" in flow.request.headers.get("X-Requested-With", "").lower():
            # Get current date parts
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")

            # Folder: logs/yyyy/mm/
            folder_path = os.path.join(self.base_log_dir, year, month)
            os.makedirs(folder_path, exist_ok=True)

            # File: mitmproxy_dd.log
            log_filename = f"mitmproxy_{day}.log"
            log_file_path = os.path.join(folder_path, log_filename)

            # Log data            
            log_entry = {
                "timestamp": now.isoformat(),
                "url": flow.request.pretty_url,
                "method": flow.request.method,
                "status_code": flow.response.status_code,
                "request_headers": dict(flow.request.headers),
                "request_payload": flow.request.get_text(), 
                "response_headers": dict(flow.response.headers),
                "response_body": flow.response.get_text()
            }

            # Append to file (or create if not exists)
            with open(log_file_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, indent=2))
                f.write("\n" + "- -" * 20 + "\n")

addons = [
    SaveXHRRequests()
]