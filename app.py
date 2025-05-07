import streamlit as st
import json

# --- Load công thức ---
with open("data/recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

st.title("🥗 Trợ lý thiết kế thực đơn thông minh")

# --- Bộ lọc chế độ ăn ---
diet_type = st.selectbox("Chọn chế độ ăn", ["Tất cả", "Ăn mặn", "Ăn chay", "Ăn thuần chay"])
if diet_type != "Tất cả":
    if diet_type == "Ăn mặn":
        recipes = [r for r in recipes if r.get("type", "mặn") == "mặn"]
    elif diet_type == "Ăn chay":
        recipes = [r for r in recipes if r.get("type") == "chay"]
    elif diet_type == "Ăn thuần chay":
        recipes = [r for r in recipes if r.get("type") == "thuần chay"]

# --- Bộ lọc độ khó ---
difficulty = st.radio("Bạn muốn món đơn giản hay cầu kỳ?", ["Tất cả", "đơn giản", "cầu kỳ"])
if difficulty != "Tất cả":
    recipes = [r for r in recipes if r.get("difficulty") == difficulty]

# --- Bộ lọc mục tiêu sức khỏe ---
goal = st.selectbox("Mục tiêu sức khỏe của bạn", ["Tất cả", "Tăng cân", "Giảm cân", "Giữ cân"])
if goal != "Tất cả":
    recipes = [r for r in recipes if r.get("goal") == goal]

# --- Bộ lọc bữa ăn ---
meal_time = st.selectbox("Chọn bữa ăn", ["Tất cả", "Sáng", "Trưa", "Tối"])
if meal_time != "Tất cả":
    recipes = [r for r in recipes if r.get("meal") == meal_time.lower()]

# --- Hiển thị kết quả ---
if recipes:
    st.subheader(f"🎉 Có {len(recipes)} món phù hợp với bạn:")
    for r in recipes:
        st.markdown(f"### 🍽️ {r['name']}")
        st.markdown(f"**Nguyên liệu:** {', '.join(r['ingredients'])}")
        st.markdown(f"**Cách làm:** {r['instructions']}")
        st.markdown(f"**Độ khó:** {r['difficulty'].capitalize()} | **Chế độ ăn:** {r['type'].capitalize()} | **Mục tiêu:** {r['goal'].capitalize()} | **Bữa ăn:** {r['meal'].capitalize()}")
        st.markdown("---")
else:
    st.warning("😥 Không tìm thấy món ăn phù hợp.")
