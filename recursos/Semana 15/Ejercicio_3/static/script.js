async function sendPrompt() {
  const prompt = document.getElementById("prompt").value;
  const responseBox = document.getElementById("response");

  responseBox.innerHTML = "Generando respuesta...";
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });

  const data = await res.json();
  responseBox.innerHTML = data.response;
}
