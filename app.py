import streamlit as st
import pandas as pd
import json

# Tải dữ liệu JSON
with open("recipes_named.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

# Chuyển sang DataFrame
df = pd.DataFrame(recipes)

st.title("Trình lọc món ăn thông minh")

# Bộ lọc loại món ăn (mặn, chay, thuần chay)
meal_type = st.selectbox("Chọn loại món ăn", ["Tất cả", "mặn", "chay", "thuần chay"])

# Bộ lọc mục tiêu sức khỏe
goal = st.selectbox("Chọn mục tiêu sức khỏe", ["Tất cả"] + sorted(df['goal'].dropna().unique().tolist()))

# Bộ lọc dị ứng (lọc nguyên liệu)
all_ingredients = sorted(set(ing for recipe in df["ingredients"] for ing in recipe))
allergy_ingredients = st.multiselect("Chọn nguyên liệu bạn dị ứng", all_ingredients)

# Bộ lọc tâm trạng
mood = st.multiselect("Tâm trạng hiện tại", sorted(set(m for moods in df["moods"] for m in moods)))

# Bộ lọc bữa ăn
meal_time = st.selectbox("Chọn bữa ăn", ["Tất cả", "sáng", "trưa", "tối"])

# Bộ lọc độ phức tạp
difficulty_levels = sorted(df["difficulty"].dropna().unique().tolist())
difficulty = st.multiselect("Chọn độ phức tạp món ăn", difficulty_levels)

# Bắt đầu lọc
filtered_df = df.copy()

if meal_type != "Tất cả":
    filtered_df = filtered_df[filtered_df["type"] == meal_type]

if goal != "Tất cả":
    filtered_df = filtered_df[filtered_df["goal"] == goal]

if allergy_ingredients:
    filtered_df = filtered_df[~filtered_df["ingredients"].apply(lambda ings: any(a in ings for a in allergy_ingredients))]

if mood:
    filtered_df = filtered_df[filtered_df["moods"].apply(lambda moods: any(m in moods for m in mood))]

if meal_time != "Tất cả":
    filtered_df = filtered_df[filtered_df["meal"] == meal_time]

if difficulty:
    filtered_df = filtered_df[filtered_df["difficulty"].isin(difficulty)]

# Hiển thị kết quả
st.subheader(f"📋 Có {len(filtered_df)} món ăn phù hợp:")
for _, row in filtered_df.iterrows():
    st.markdown(f"### 🍽️ {row['name']}")
    st.markdown(f"- **Loại**: {row['type'].capitalize()}")
    st.markdown(f"- **Mục tiêu**: {row['goal']}")
    st.markdown(f"- **Bữa ăn**: {row['meal']}")
    st.markdown(f"- **Tâm trạng phù hợp**: {', '.join(row['moods'])}")
    st.markdown(f"- **Độ phức tạp**: {row['difficulty']}")
    st.markdown(f"- **Nguyên liệu**: {', '.join(row['ingredients'])}")
    st.markdown(f"- **Cách nấu**: {row['instructions']}")
    st.markdown("---")

if len(filtered_df) == 0:
    st.warning("😕 Không tìm thấy món ăn phù hợp với tiêu chí đã chọn.")
