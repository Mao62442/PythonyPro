const socket = new WebSocket("ws://" + window.location.host + "/ws/data");

socket.onopen = () => console.log("✅ 接続成功");
socket.onmessage = event => {
    const data = JSON.parse(event.data);
    document.getElementById("formaldehyde").innerText = data.formaldehyde || "---";
    document.getElementById("temperature").innerText = data.temperature || "---";
    document.getElementById("humidity").innerText = data.humidity || "---";
};
socket.onerror = err => console.error("❌ WebSocketエラー:", err);
socket.onclose = () => console.warn("🔌 WebSocket切断");