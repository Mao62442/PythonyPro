// ページの読み込みが完了したら実行
document.addEventListener('DOMContentLoaded', (event) => {

    // グラフ描画のための設定
    const commonChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        animation: false, // アニメーションを無効にしてパフォーマンスを向上
        plugins: {
            legend: {display: false},
            tooltip: {enabled: true}
        },
        interaction: {
            mode: 'nearest',
            intersect: false
        },
        scales: {
            x: {
                type: 'time',
                time: {
                    parser: 'YYYY-MM-DD HH:mm:ss', // CSVのタイムスタンプ形式
                    tooltipFormat: 'HH:mm', // ツールチップのフォーマットは詳細なまま
                    unit: 'hour', // ★変更点：時間単位で表示
                    displayFormats: {
                        hour: 'HH:00' // ★変更点：時間の表示フォーマット
                    }
                },
                ticks: {
                    source: 'auto',
                    maxRotation: 0,
                    autoSkip: true,
                }
            },
            y: {
                beginAtZero: true,
                grid: {display: true}
            }
        }
    };

    // ホルムアルデヒドグラフの初期化
    const chartFormaldehyde = new Chart(document.getElementById('chart-formaldehyde'), {
        type: 'line',
        data: {
            datasets: [{
                label: 'ホルムアルデヒド濃度[PPM]',
                data: [],
                borderColor: 'rgba(60, 110, 133, 1)',
                borderWidth: 2,
                pointRadius: 1,
                fill: false // 陰影を非表示
            }]
        },
        options: commonChartOptions
    });

    // 温度グラフの初期化
    const chartTemperature = new Chart(document.getElementById('chart-temperature'), {
        type: 'line',
        data: {
            datasets: [{
                label: '温度[℃]',
                data: [],
                borderColor: 'rgba(60, 110, 133, 1)',
                borderWidth: 2,
                pointRadius: 1,
                fill: false // 陰影を非表示
            }]
        },
        options: commonChartOptions
    });

    // 湿度グラフの初期化
    const chartHumidity = new Chart(document.getElementById('chart-humidity'), {
        type: 'line',
        data: {
            datasets: [{
                label: '湿度[%]',
                data: [],
                borderColor: 'rgba(60, 110, 133, 1)',
                borderWidth: 2,
                pointRadius: 1,
                fill: false // 陰影を非表示
            }]
        },
        options: commonChartOptions
    });

    // WebSocket接続
    const ws_history_data = new WebSocket("ws://" + window.location.host + "/ws/history");
    const ws_now_data = new WebSocket("ws://" + window.location.host + "/ws/now_data");

    ws_history_data.onopen = () => console.log("✅ WebSocket接続成功 (History)");
    ws_history_data.onerror = err => console.error("❌ WebSocketエラー:", err);
    ws_history_data.onclose = () => console.warn("🔌 WebSocket切断");

    ws_now_data.onopen = () => console.log("✅ WebSocket接続成功 (Now)");
    ws_now_data.onerror = err => console.error("❌ WebSocketエラー:", err);
    ws_now_data.onclose = () => console.warn("🔌 WebSocket切断");

    // サーバーからメッセージを受信したときの処理
    ws_history_data.onmessage = function (event) {
        const json = JSON.parse(event.data);
        const historyData = json.data; // { "data": [...] } の "data" 配列を取得

        if (!historyData || historyData.length === 0) {
            console.log("データが空です。");
            return;
        }

        // グラフ用のデータを作成
        const formaldehydeData = [];
        const temperatureData = [];
        const humidityData = [];

        historyData.forEach(row => {
            // Luxonを使ってタイムスタンプをパース
            const timestamp = luxon.DateTime.fromSQL(row.timestamp).valueOf();

            formaldehydeData.push({x: timestamp, y: parseFloat(row.formaldehyde)});
            temperatureData.push({x: timestamp, y: parseFloat(row.temperature)});
            humidityData.push({x: timestamp, y: parseFloat(row.humidity)});
        });

        // 各グラフのデータを更新
        chartFormaldehyde.data.datasets[0].data = formaldehydeData;
        chartTemperature.data.datasets[0].data = temperatureData;
        chartHumidity.data.datasets[0].data = humidityData;

        // すべてのグラフを再描画
        chartFormaldehyde.update();
        chartTemperature.update();
        chartHumidity.update();
    };

    ws_now_data.onmessage = function (event) {
        const nowDataJson = JSON.parse(event.data);
        document.getElementById("formaldehyde").innerText = nowDataJson.formaldehyde || "---";
        document.getElementById("temperature").innerText = nowDataJson.temperature || "---";
        document.getElementById("humidity").innerText = nowDataJson.humidity || "---";

        const alert_corner = document.getElementById("alert-corner");
        if(nowDataJson.formaldehyde >= 0.03) {
            alert_corner.innerHTML = `
                <p style="color: red; font-weight: bold; margin-bottom: 10px;">濃度基準値オーバー</p>
                <img id="alert-icon" src="../static/img/alert.png"/>`
        } else {
            const alert_corner = document.getElementById("alert-corner");
            alert_corner.innerHTML = ``
        }
    }

});