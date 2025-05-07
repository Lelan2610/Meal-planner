import streamlit as st
import json

# --- Load công thức ---
with open("data/recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

st.title("🥗 Trợ lý thiết kế thực đơn thông minh")

# --- Mục tiêu sức khỏe ---
goal = st.selectbox("Mục tiêu của bạn là gì?", ["Tất cả", "Tăng cân", "Giảm cân", "Giữ cân"])
if goal != "Tất cả":
    recipes = [r for r in recipes if goal.lower() in r.get("goal", [])]

# --- Bộ lọc chế độ ăn ---
diet_type = st.selectbox("Chọn chế độ ăn", ["Tất cả", "Ăn mặn", "Ăn chay", "Ăn thuần chay"])
if diet_type != "Tất cả":
    recipes = [r for r in recipes if r.get("type", "mặn") == diet_type.replace("Ăn ", "")]

# --- Bộ lọc độ khó ---
difficulty = st.radio("Bạn muốn món đơn giản hay cầu kỳ?", ["Tất cả", "đơn giản", "cầu kỳ"])
if difficulty != "Tất cả":
    recipes = [r for r in recipes if r.get("difficulty") == difficulty]

# --- Tâm trạng ---
mood = st.selectbox("Tâm trạng của bạn hôm nay là gì?", ["Tất cả", "vui", "buồn", "căng thẳng", "bình thường"])
if mood != "Tất cả":
    recipes = [r for r in recipes if mood in r.get("moods", [])]

# --- Hiển thị kết quả ---
if recipes:
    st.subheader(f"🎉 Có {len(recipes)} món phù hợp với bạn:")
    for r in recipes:
        st.markdown(f"### 🍽️ {r['name']}")
        st.markdown(f"**Nguyên liệu:** {', '.join(r['ingredients'])}")
        st.markdown(f"**Cách làm:** {r['instructions']}")
        st.markdown(f"**Độ khó:** {r['difficulty'].capitalize()} | **Chế độ ăn:** {r['type'].capitalize()} | **Mục tiêu:** {', '.join(r['goal'])}")
        st.markdown("---")
else:
    st.warning("😥 Không tìm thấy món ăn phù hợp.")
