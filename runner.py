from rentogram import app


if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG"), host="0.0.0.0", port=app.config.get("APP_PORT"))
