import streamlit as st
from utils.recipe_generator import get_daily_meal_plan
from utils.nutrition import calculate_tdee
import json

# Load dữ liệu công thức
with open("data/recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

st.title("🍽️ Trợ lý Thực đơn Cá nhân")
st.markdown(
    """
    <div style='text-align: right'>
        🔗 <a href="https://github.com/your-username/meal-planner-streamlit" target="_blank">Xem mã nguồn trên GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Nhập thông tin người dùng
weight = st.number_input("Cân nặng (kg)", 30, 200)
height = st.number_input("Chiều cao (cm)", 100, 220)
age = st.number_input("Tuổi", 10, 100)
gender = st.selectbox("Giới tính", ["male", "female"])
goal = st.selectbox("Mục tiêu", ["Tăng cân", "Giảm cân", "Giữ cân"])
mood = st.selectbox("Tâm trạng hôm nay", ["Bình thường", "Căng thẳng", "Vui", "Buồn"])
preference = st.radio("Bạn muốn món ăn...", ["đơn giản", "cầu kỳ"])
allergies = st.text_input("Bạn dị ứng với gì? (cách nhau bằng dấu phẩy)").split(",")

activity_level = 1.2  # Mặc định

if st.button("Gợi ý thực đơn"):
    tdee = calculate_tdee(weight, height, age, gender, activity_level)
    user_input = {
        "preference": preference,
        "allergies": [a.strip().lower() for a in allergies if a.strip()],
        "mood": mood.lower()
    }
    meals = get_daily_meal_plan(user_input, recipes)

    st.subheader(f"🌟 Gợi ý thực đơn (TDEE ~ {int(tdee)} kcal/ngày):")
    if meals:
        for meal in meals:
            st.markdown(f"### {meal['name']}")
            st.markdown(f"- **Nguyên liệu:** {', '.join(meal['ingredients'])}")
            st.markdown(f"- **Cách làm:** {meal['instructions']}")
            st.markdown(f"- **Độ khó:** {meal['difficulty']}")
    else:
        st.warning("Không tìm thấy công thức phù hợp. Hãy thử thay đổi tuỳ chọn!")
