import streamlit as st
import pandas as pd

st.set_page_config(page_title="Burst Bar Comment Manager", 
                   page_icon="💬", layout="centered")

st.markdown("# 💬 Burst Bar Comment Manager")
st.markdown("Review, edit, and copy comments to post on Instagram.")
st.markdown("---")

uploaded_file = st.file_uploader("Upload your comments.xlsx", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if "Category" not in df.columns or "Comment" not in df.columns:
        st.error("Your Excel file must have 'Category' and 'Comment' columns.")
    else:
        categories = ["All"] + sorted(df["Category"].unique().tolist())
        selected = st.selectbox("Filter by category", categories)

        if selected != "All":
            filtered = df[df["Category"] == selected].reset_index(drop=True)
        else:
            filtered = df.reset_index(drop=True)

        st.markdown(f"### {len(filtered)} comments found")
        st.markdown("---")

        for i, row in filtered.iterrows():
            with st.container():
                st.markdown(f"**Category:** `{row['Category']}`")
                
                edited = st.text_area(
                    label=f"Comment {i+1}",
                    value=row["Comment"],
                    height=80,
                    key=f"comment_{i}"
                )

                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button(f"📋 Copy", key=f"copy_{i}"):
                        st.code(edited, language=None)
                        st.success("⬆️ Select the text above and copy it (Ctrl+C)")
                
                st.markdown("---")

        st.markdown("### ➕ Add a New Comment")
        new_category = st.text_input("Category", placeholder="e.g. Motivational")
        new_comment = st.text_area("Comment", placeholder="Type your comment here...")
        
        if st.button("Add to list"):
            if new_category and new_comment:
                new_row = pd.DataFrame([[new_category, new_comment]], 
                                        columns=["Category", "Comment"])
                df = pd.concat([df, new_row], ignore_index=True)
                st.success("✅ Added! Download the updated file below.")
                
                from io import BytesIO
                output = BytesIO()
                df.to_excel(output, index=False)
                st.download_button(
                    label="📥 Download updated comments.xlsx",
                    data=output.getvalue(),
                    file_name="comments.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning("Please fill in both fields.")

else:
    st.info("👆 Upload your comments.xlsx file to get started.")
    
    st.markdown("### 📝 Your Excel file should look like this:")
    sample = pd.DataFrame({
        "Category": ["General", "Quit Journey", "Savings", "Motivational"],
        "Comment": [
            "Love this product! 🔥",
            "So proud of everyone taking this step 💪",
            "Imagine what you could do with that money back! 💸",
            "Day 1 is the hardest. You've got this! 🙌"
        ]
    })
    st.dataframe(sample, use_container_width=True)
```

---

## Step 3 — Update `requirements.txt`

Edit your `requirements.txt` on GitHub to contain:
```
streamlit
requests
openpyxl
pandas
