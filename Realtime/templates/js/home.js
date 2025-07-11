// CSVファイルのパス
const csvFilePath = 'data.csv'; // このファイルをウェブサーバーの同じ階層に配置してください

// データを表示する要素のID
const formaldehydeElem = document.getElementById('formaldehyde-data');
const temperatureElem = document.getElementById('temperature-data');
const humidityElem = document.getElementById('humidity-data');

// CSVデータを読み込んで表示を更新する関数
async function updateCurrentData() {
    try {
        const response = await fetch(csvFilePath);
        if (!response.ok) {
            throw new Error(`CSVファイルの読み込みに失敗しました: ${response.statusText}`);
        }
        const csvText = await response.text();

        // CSVデータを解析（簡易的なカンマ区切り）
        const lines = csvText.trim().split('\n');
        const data = {};
        lines.forEach(line => {
            const parts = line.split(',');
            if (parts.length >= 2) {
                data[parts[0].trim()] = parts[1].trim();
            }
        });

        // 各要素のテキストを更新
        if (data['ホルムアルデヒド濃度']) {
            formaldehydeElem.textContent = `現時点ホルムアルデヒド濃度 : ${data['ホルムアルデヒド濃度']} [PPM]`;
        }
        if (data['温度']) {
            temperatureElem.textContent = `現時点温度 : ${data['温度']}°C`;
        }
        if (data['湿度']) {
            humidityElem.textContent = `現時点湿度 : ${data['湿度']}%`;
        }

    } catch (error) {
        console.error("データの更新中にエラーが発生しました:", error);
        formaldehydeElem.textContent = '現時点ホルムアルデヒド濃度 : エラー';
        temperatureElem.textContent = '現時点温度 : エラー';
        humidityElem.textContent = '現時点湿度 : エラー';
    }
}

// ページ読み込み時に一度データを表示
updateCurrentData();

// 5秒ごとにデータを更新（ポーリング）
// 必要に応じて更新間隔 (ミリ秒) を調整してください
setInterval(updateCurrentData, 5000); // 5000ミリ秒 = 5秒