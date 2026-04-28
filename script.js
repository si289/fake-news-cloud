<script>
function checkNews() {
    let newsText = document.getElementById("newsInput").value;

    fetch(fetch("https://fake-news-cloud-3.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: newsText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "Prediction: " + data.prediction +
            "<br>Confidence: " + data.confidence + "%";
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Server error!");
    });
}
</script>

        