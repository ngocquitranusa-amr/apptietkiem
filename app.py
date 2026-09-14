<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>App Tiết Kiệm</title>
<style>
body {
    font-family: Arial;
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    text-align: center;
}

input, button {
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    box-sizing: border-box;
}

button {
    cursor: pointer;
    background: #222;
    color: white;
    border: none;
    border-radius: 6px;
}

#balance {
    font-size: 28px;
    font-weight: bold;
}
</style>
</head>

<body>

<h1>💰 Tiết Kiệm</h1>

<p>Số tiền đang tiết kiệm:</p>
<div id="balance">0 VNĐ</div>

<input id="amount" type="number" placeholder="Nhập số tiền muốn nạp">

<p>Chọn ngày được phép rút:</p>
<input id="unlockDate" type="date">

<button onclick="deposit()">🔒 Nạp tiền & khóa</button>

<button onclick="withdraw()">💸 Rút tiền</button>

<p id="message"></p>

<script>

let saving = JSON.parse(localStorage.getItem("saving")) || {
    amount: 0,
    unlockDate: null
};

function updateScreen() {
    document.getElementById("balance").innerText =
        saving.amount.toLocaleString("vi-VN") + " VNĐ";
}

function deposit() {

    let amount = Number(document.getElementById("amount").value);
    let date = document.getElementById("unlockDate").value;

    if (amount <= 0 || !date) {
        alert("Vui lòng nhập số tiền và ngày rút!");
        return;
    }

    saving.amount += amount;
    saving.unlockDate = new Date(date + "T00:00:00").getTime();

    localStorage.setItem("saving", JSON.stringify(saving));

    document.getElementById("message").innerText =
        "🔒 Đã khóa tiền đến ngày " +
        new Date(saving.unlockDate).toLocaleDateString("vi-VN");

    updateScreen();
}

function withdraw() {

    if (saving.amount <= 0) {
        alert("Bạn chưa có tiền tiết kiệm!");
        return;
    }

    if (Date.now() < saving.unlockDate) {

        alert(
            "🔒 Chưa đến ngày được rút!\n\n" +
            "Ngày được rút: " +
            new Date(saving.unlockDate).toLocaleDateString("vi-VN")
        );

        return;
    }

    alert(
        "✅ Rút thành công " +
        saving.amount.toLocaleString("vi-VN") +
        " VNĐ"
    );

    saving.amount = 0;
    saving.unlockDate = null;

    localStorage.setItem("saving", JSON.stringify(saving));

    updateScreen();
}

updateScreen();

</script>

</body>
</html>
