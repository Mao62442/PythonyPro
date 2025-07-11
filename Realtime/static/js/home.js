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

const ws = new WebSocket("ws://" + location.host + "/ws/data");

// 各グラフ用データ配列
const labels = [];
const dataFormaldehyde = [];
const dataTemperature = [];
const dataHumidity = [];

// 各チャート初期化
const chartFormaldehyde = new Chart(document.getElementById('chart-formaldehyde'), {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'ホルムアルデヒド濃度 (PPM)',
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            data: dataFormaldehyde
        }]
    },
    options: { animation: false, responsive: true }
});

const chartTemperature = new Chart(document.getElementById('chart-placeholder'), {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: '温度 (℃)',
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            data: dataTemperature
        }]
    },
    options: { animation: false, responsive: true }
});

const chartHumidity = new Chart(document.getElementById('chart-humidity'), {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: '湿度 (%)',
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            data: dataHumidity
        }]
    },
    options: { animation: false, responsive: true }
});

ws.onmessage = function(event) {
    const msg = JSON.parse(event.data);
    const now = new Date().toLocaleTimeString();

    // DOMにも最新値表示
    document.getElementById('formaldehyde').textContent = msg.formaldehyde;
    document.getElementById('temperature').textContent = msg.temperature;
    document.getElementById('humidity').textContent = msg.humidity;

    // 最大50件に制限
    if (labels.length >= 50) {
        labels.shift();
        dataFormaldehyde.shift();
        dataTemperature.shift();
        dataHumidity.shift();
    }

    // グラフに新データ追加
    labels.push(now);
    dataFormaldehyde.push(parseFloat(msg.formaldehyde));
    dataTemperature.push(parseFloat(msg.temperature));
    dataHumidity.push(parseFloat(msg.humidity));

    chartFormaldehyde.update();
    chartTemperature.update();
    chartHumidity.update();
};
