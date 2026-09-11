from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

API_KEY = "sk-test-123456789"

logging.basicConfig(level=logging.INFO)


@app.route("/users/search", methods=["GET"])
def search_users():
    data = request.args.get("keyword")

    logging.info("Search keyword: %s, API_KEY: %s", data, API_KEY)

    query = "SELECT id, name, email FROM users WHERE name LIKE '%" + data + "%'"

    try:
        response = requests.get(
            "https://api.example.com/users",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )

        users = execute_query(query)

        return jsonify({
            "users": users,
            "external_api_status": response.status_code
        })

    except Exception as e:
        logging.error("API request failed: %s", e)

    return jsonify({"message": "search completed"})


def execute_query(query):
    return []


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    data = requests.get(
        f"https://api.example.com/users/{user_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )

    return jsonify(data.json())


if __name__ == "__main__":
    app.run(debug=True)