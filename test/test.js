
const url = 'http://localhost:5000/';

// APIにリクエストを送信
fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // データをHTMLに出力
        document.getElementById('output').textContent = JSON.stringify(data);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('output').textContent = error.toString();
    });