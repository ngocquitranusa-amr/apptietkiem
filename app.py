import streamlit as st
from datetime import date

# ==========================================
# CẤU HÌNH
# ==========================================
st.set_page_config(
    page_title="MoneyGo - Học & Tiết Kiệm",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# CSS - GIAO DIỆN KIỂU APP HỌC TẬP
# ==========================================
st.markdown("""
<style>
    .main {
        background-color: #f7f7f7;
    }

    .title {
        font-size: 40px;
        font-weight: 800;
        text-align: center;
        color: #58cc02;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    .money {
        font-size: 32px;
        font-weight: 800;
        color: #58cc02;
    }

    .xp {
        font-size: 24px;
        font-weight: bold;
        color: #ff9600;
    }

    .streak {
        font-size: 24px;
        font-weight: bold;
        color: #ff4b4b;
    }

    .level {
        font-size: 24px;
        font-weight: bold;
        color: #7c4dff;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================
if "money" not in st.session_state:
    st.session_state.money = 0

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "streak" not in st.session_state:
    st.session_state.streak = 1

if "level" not in st.session_state:
    st.session_state.level = 1

if "goal" not in st.session_state:
    st.session_state.goal = 10_000_000

# ==========================================
# TIÊU ĐỀ
# ==========================================
st.markdown('<div class="title">💰 MoneyGo</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Học kỹ năng tài chính • Hoàn thành nhiệm vụ • Xây dựng khoản tiết kiệm</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("📱 MoneyGo")

menu = st.sidebar.radio(
    "Chọn chức năng",
    [
        "🏠 Trang chủ",
        "📚 Học tài chính",
        "🎯 Nhiệm vụ",
        "💰 Tiết kiệm",
        "🏆 Thành tích"
    ]
)

# ==========================================
# TRANG CHỦ
# ==========================================
if menu == "🏠 Trang chủ":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f'<div class="card"><div class="xp">⭐ {st.session_state.xp} XP</div><small>Kinh nghiệm</small></div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f'<div class="card"><div class="streak">🔥 {st.session_state.streak}</div><small>Ngày liên tiếp</small></div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f'<div class="card"><div class="level">🏅 Level {st.session_state.level}</div><small>Cấp độ</small></div>',
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f'<div class="card"><div class="money">{st.session_state.money:,.0f}đ</div><small>Tiền tiết kiệm</small></div>',
            unsafe_allow_html=True
        )

    st.subheader("🎯 Mục tiêu tiết kiệm")

    progress = min(st.session_state.money / st.session_state.goal, 1)

    st.progress(progress)

    st.write(
        f"Đã tiết kiệm: **{st.session_state.money:,.0f}đ** / "
        f"**{st.session_state.goal:,.0f}đ**"
    )

    st.divider()

    st.subheader("📅 Nhiệm vụ hôm nay")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📚 Học 1 bài tài chính\n\n+20 XP")

    with col2:
        st.info("💰 Tiết kiệm hôm nay\n\n+30 XP")

    with col3:
        st.info("🧠 Làm bài kiểm tra\n\n+50 XP")

# ==========================================
# HỌC TÀI CHÍNH
# ==========================================
elif menu == "📚 Học tài chính":

    st.header("📚 Học tài chính")

    lessons = [
        "💵 Bài 1: Tiền là gì?",
        "🏦 Bài 2: Tiết kiệm",
        "📈 Bài 3: Lãi suất",
        "💳 Bài 4: Quản lý chi tiêu",
        "📊 Bài 5: Đầu tư cơ bản"
    ]

    for i, lesson in enumerate(lessons):

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(lesson)

        if st.button(
            "Bắt đầu học",
            key=f"lesson_{i}"
        ):
            st.session_state.xp += 20

            st.success(
                f"🎉 Hoàn thành bài học! +20 XP\n\n"
                f"Tổng XP: {st.session_state.xp}"
            )

        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# NHIỆM VỤ
# ==========================================
elif menu == "🎯 Nhiệm vụ":

    st.header("🎯 Nhiệm vụ hôm nay")

    st.write("Hoàn thành nhiệm vụ để nhận XP và duy trì streak.")

    task1 = st.checkbox("📚 Học một bài tài chính (+20 XP)")
    task2 = st.checkbox("💰 Tiết kiệm tiền hôm nay (+30 XP)")
    task3 = st.checkbox("🧠 Trả lời câu hỏi (+50 XP)")

    if st.button("🎁 Nhận XP"):

        xp_gain = 0

        if task1:
            xp_gain += 20

        if task2:
            xp_gain += 30

        if task3:
            xp_gain += 50

        st.session_state.xp += xp_gain

        st.success(
            f"🎉 Bạn nhận được +{xp_gain} XP!"
        )

# ==========================================
# TIẾT KIỆM
# ==========================================
elif menu == "💰 Tiết kiệm":

    st.header("💰 Ví tiết kiệm")

    st.markdown(
        f"""
        <div class="card">
            <div>💰 Số tiền hiện tại</div>
            <div class="money">
                {st.session_state.money:,.0f}đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("➕ Thêm tiền tiết kiệm")

    amount = st.number_input(
        "Số tiền muốn thêm",
        min_value=0,
        step=10_000,
        value=100_000
    )

    if st.button("💵 Gửi vào quỹ"):

        if amount > 0:

            st.session_state.money += amount
            st.session_state.xp += 30

            st.success(
                f"Đã thêm {amount:,.0f}đ vào quỹ tiết kiệm! "
                f"+30 XP 🎉"
            )

    st.divider()

    st.subheader("🎯 Mục tiêu tiết kiệm")

    new_goal = st.number_input(
        "Nhập mục tiêu",
        min_value=100_000,
        step=100_000,
        value=st.session_state.goal
    )

    if st.button("Lưu mục tiêu"):
        st.session_state.goal = new_goal
        st.success("Đã cập nhật mục tiêu!")

    progress = min(
        st.session_state.money / st.session_state.goal,
        1
    )

    st.progress(progress)

    st.write(
        f"Tiến độ: **{progress * 100:.1f}%**"
    )

    if progress >= 1:
        st.balloons()
        st.success("🏆 CHÚC MỪNG! Bạn đã đạt mục tiêu!")

# ==========================================
# THÀNH TÍCH
# ==========================================
elif menu == "🏆 Thành tích":

    st.header("🏆 Thành tích")

    achievements = [
        ("🌱", "Khởi đầu", "Bắt đầu hành trình tài chính"),
        ("🔥", "7 ngày liên tiếp", "Duy trì streak 7 ngày"),
        ("💰", "Người tiết kiệm", "Tiết kiệm được 1 triệu"),
        ("🏦", "Kỷ luật tài chính", "Hoàn thành 20 nhiệm vụ"),
        ("👑", "Money Master", "Đạt Level 10")
    ]

    for icon, name, description in achievements:

        st.markdown(
            f"""
            <div class="card">
                <h3>{icon} {name}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

st.caption(
    f"MoneyGo • XP: {st.session_state.xp} • "
    f"Level: {st.session_state.level} • "
    f"Tiết kiệm: {st.session_state.money:,.0f}đ"
)
