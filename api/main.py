"""
Toolkit Access Request API — Cloud Run Service
Receives form submissions from the onboarding site and emails Jake
via Domo Code Engine sendEmail function.
"""

import os
import logging
import requests as http_requests
from flask import Flask, request, jsonify
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("toolkit-api")

app = Flask(__name__)
CORS(app, origins=[
    "https://jakeheaps-coder.github.io",
    "http://localhost:*",
    "http://127.0.0.1:*"
])

DOMO_INSTANCE = os.environ.get("DOMO_INSTANCE", "domo.domo.com")
DOMO_ACCESS_TOKEN = os.environ.get("DOMO_ACCESS_TOKEN", "")
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "jake.heaps@domo.com")

# Domo Code Engine email function (same as weekly executive report)
CE_EMAIL_PACKAGE_ID = "03ba6971-98d0-4654-9bfd-aa897816df33"
CE_EMAIL_VERSION = "2.1.13"


def send_email_via_domo(to_emails: str, subject: str, body_html: str) -> bool:
    """Send email via Domo Code Engine sendEmail function."""
    url = (
        f"https://{DOMO_INSTANCE}/api/codeengine/v2/packages/"
        f"{CE_EMAIL_PACKAGE_ID}/versions/{CE_EMAIL_VERSION}/functions/sendEmail"
    )
    headers = {
        "X-DOMO-Developer-Token": DOMO_ACCESS_TOKEN,
        "Content-Type": "application/json",
    }
    payload = {
        "inputVariables": {
            "recipientEmails": to_emails,
            "subject": subject,
            "body": body_html,
        },
        "settings": {"getLogs": False},
    }

    try:
        resp = http_requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code < 300:
            logger.info(f"Email sent to {to_emails} via Code Engine")
            return True
        else:
            logger.warning(f"Email failed ({resp.status_code}): {resp.text[:300]}")
            return False
    except Exception as e:
        logger.warning(f"Email failed: {e}")
        return False


# In-memory store for requests
_requests_log = []


@app.route("/api/request-access", methods=["POST"])
def request_access():
    """Handle toolkit access request form submission."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "").strip()
    username = data.get("username", "").strip()
    role = data.get("role", "Unknown").strip()

    if not name or not username:
        return jsonify({"error": "Name and GitHub username are required"}), 400

    # Always log
    logger.info(f"ACCESS REQUEST: name={name}, username={username}, role={role}")
    _requests_log.append({
        "name": name, "username": username, "role": role,
        "page": data.get("page", "Unknown"),
    })

    subject = f"Domo Toolkit Access Request - {role}: {name}"
    body_html = f"""
    <h2>New Toolkit Access Request</h2>
    <table style="border-collapse:collapse; font-family:Arial,sans-serif;">
        <tr><td style="padding:6px 12px; font-weight:bold;">Name:</td><td style="padding:6px 12px;">{name}</td></tr>
        <tr><td style="padding:6px 12px; font-weight:bold;">GitHub Username:</td><td style="padding:6px 12px;">{username}</td></tr>
        <tr><td style="padding:6px 12px; font-weight:bold;">Role:</td><td style="padding:6px 12px;">{role}</td></tr>
        <tr><td style="padding:6px 12px; font-weight:bold;">Page:</td><td style="padding:6px 12px;">{data.get('page', 'Unknown')}</td></tr>
    </table>
    <br>
    <p><strong>Action needed:</strong></p>
    <ol>
        <li>Add <strong>{username}</strong> as a collaborator: <a href="https://github.com/jakeheaps-coder/domo-toolkit/settings/access">GitHub Settings</a></li>
        <li>Add to users.json with role: <strong>{role.lower()}</strong></li>
    </ol>
    <p style="color:#888; font-size:12px;">Sent from the Domo Toolkit onboarding page.</p>
    """

    email_sent = send_email_via_domo(NOTIFY_EMAIL, subject, body_html)

    return jsonify({
        "success": True,
        "message": "Request sent to Jake" if email_sent else "Request logged. Jake will be notified.",
        "email_sent": email_sent
    })


@app.route("/api/requests", methods=["GET"])
def list_requests():
    """List all access requests (for Jake to check)."""
    return jsonify({"requests": _requests_log, "count": len(_requests_log)})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "toolkit-access-api"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
