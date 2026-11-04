
function setExample(text) {
    document.getElementById("inputText").value = text;
    document.getElementById("output").textContent =
        "Ready to predict...";
}

async function predictWord() {
    const input = document.getElementById("inputText").value.trim();
    const output = document.getElementById("output");

    if (!input) {
        output.textContent = "Please enter some text.";
        return;
    }

    output.textContent = "Predicting...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: input })
        });

        const data = await response.json();

        if (!response.ok) {
            output.textContent = data.prediction || "Prediction failed.";
            return;
        }

        output.textContent = data.prediction;

    } catch (error) {
        output.textContent =
            "Could not connect to the server. Please restart the website.";
        console.error(error);
    }
}
