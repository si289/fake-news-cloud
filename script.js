function checkNews() {
    const newsText = document.getElementById("newsInput").value;

    // Check if input is empty
    if (newsText.trim() === "") {
        document.getElementById("result").innerText = "⚠️ Please enter some news text!";
        return;
    }

    // Show loading message
    document.getElementById("result").innerText = "⏳ Checking news...";

    fetch("https://fake-news-cloud-3.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: newsText })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server error");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("result").innerText = "🧠 Result: " + data.prediction;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "❌ Error connecting to server!";
    });
}