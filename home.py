
import streamlit as st
from database import c, conn

st.title("📢 Marketplace")

# ===== BANNER ADS =====
banners = c.execute("""
SELECT * FROM banner_ads
WHERE expires_at > date('now')
LIMIT 10
""").fetchall()

st.subheader("🔥 Sponsored (UGX 40,000/week)")

cols = st.columns(len(banners) if banners else 1)

for i, b in enumerate(banners):
    with cols[i]:
        if ".mp4" in b[1]:
            st.video(b[1])
        else:
            st.image(b[1], use_column_width=True)

        st.markdown(f"[Visit Sponsor]({b[2]})")

# ===== ADS =====
ads = c.execute("""
SELECT * FROM ads
WHERE expires_at > date('now')
ORDER BY is_featured DESC
""").fetchall()

for ad in ads:
    st.markdown(f"<div class='card {'featured' if ad[5] else ''}'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:
        if ".mp4" in ad[4]:
            st.video(ad[4])
        else:
            st.image(ad[4], use_column_width=True)

    with col2:
        st.subheader(ad[2])
        st.write(ad[3])

        if ad[5]:
            st.success("⭐ Featured (UGX 20,000/week)")

        if st.button(f"View {ad[0]}"):
            c.execute("UPDATE ads SET clicks = clicks + 1 WHERE id=?", (ad[0],))
            conn.commit()

        st.markdown(f"[📲 WhatsApp](https://wa.me/{ad[1]})")
        st.markdown(f"[📞 Call](tel:{ad[1]})")
        st.markdown(f"🔗 https://yourdomain.com/ad/{ad[0]}")

        rating = st.slider("Rate Vendor",1,5,3,key=ad[0])
        if st.button("Submit", key=f"s{ad[0]}"):
            c.execute("INSERT INTO ratings(vendor_id,rating) VALUES(?,?)",
                      (ad[1], rating))
            conn.commit()

    st.markdown("</div>", unsafe_allow_html=True)
