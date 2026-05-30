from flask import Flask, render_template, request

from cipher import (
    CaesarCipher,
    AESCipher
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        text = request.form.get("text")

        key = request.form.get("key")

        algorithm = request.form.get(
            "algorithm"
        )

        action = request.form.get(
            "action"
        )

        try:

            if algorithm == "caesar":

                shift = int(key)

                if action == "encrypt":

                    result = CaesarCipher.encrypt(
                        text,
                        shift
                    )

                else:

                    result = CaesarCipher.decrypt(
                        text,
                        shift
                    )

            elif algorithm == "aes":

                aes = AESCipher(key)

                if action == "encrypt":

                    result = aes.encrypt(
                        text
                    )

                else:

                    result = aes.decrypt(
                        text
                    )

        except Exception as e:

            result = f"Error: {e}"

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)