function guiTien(soTien, ngayRut) {
    const ngayHienTai = new Date();

    const khoanTietKiem = {
        soTien: soTien,
        ngayGui: ngayHienTai,
        ngayDuocRut: new Date(ngayRut),
        daRut: false
    };

    localStorage.setItem(
        "khoanTietKiem",
        JSON.stringify(khoanTietKiem)
    );

    console.log("Đã khóa tiền đến ngày: " + ngayRut);
}

function rutTien() {
    const data = JSON.parse(
        localStorage.getItem("khoanTietKiem")
    );

    if (!data) {
        alert("Chưa có khoản tiết kiệm!");
        return;
    }

    const homNay = new Date();
    const ngayDuocRut = new Date(data.ngayDuocRut);

    if (homNay < ngayDuocRut) {
        alert(
            "Chưa đến ngày rút tiền!\n" +
            "Bạn chỉ được rút vào: " +
            ngayDuocRut.toLocaleDateString("vi-VN")
        );
        return;
    }

    if (data.daRut) {
        alert("Khoản tiền này đã được rút.");
        return;
    }

    data.daRut = true;
    localStorage.setItem(
        "khoanTietKiem",
        JSON.stringify(data)
    );

    alert("Rút tiền thành công: " + data.soTien + " VNĐ");
}
