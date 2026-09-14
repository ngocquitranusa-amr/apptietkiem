function deposit(amount, unlockDate) {
    const saving = {
        amount: amount,
        unlockDate: new Date(unlockDate).getTime()
    };

    localStorage.setItem("saving", JSON.stringify(saving));
}

function withdraw() {
    const saving = JSON.parse(localStorage.getItem("saving"));

    if (!saving) return alert("Không có tiền tiết kiệm!");

    if (Date.now() < saving.unlockDate) {
        return alert("🔒 Tiền đang bị khóa, chưa đến ngày được rút!");
    }

    alert(`💰 Rút thành công ${saving.amount.toLocaleString()} VNĐ`);
    localStorage.removeItem("saving");
}
