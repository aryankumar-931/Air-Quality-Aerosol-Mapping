import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import folium
from streamlit_folium import folium_static
from datetime import date

def generate_pdf_report(start_date, end_date,layer_name,avg_value,image_count):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Air Quality & Aerosol Mapping Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Date Range:</b> {start_date} to {end_date}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Layer:</b> {layer_name}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Average Value:</b> {avg_value}",
            styles["Normal"]
        )
    )
    elements.append(
        Paragraph(
            f"<b>Images Used:</b> {image_count}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

from src.air_quality_layers import (
    get_aod_layer,
    get_no2_layer,
    get_aod_stats,
    get_no2_stats
)

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Air Quality & Aerosol Mapping",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------------
# HEADER
# ----------------------------------

st.title("🌍 Air Quality & Aerosol Mapping")

st.markdown("""
### Satellite-Based Air Quality Monitoring

This dashboard visualizes:

- 🌫️ MODIS Aerosol Optical Depth (AOD)
- 🏭 Sentinel-5P NO₂ Concentration

using Google Earth Engine.
""")

# ----------------------------------
# DATE FILTERS
# ----------------------------------

st.sidebar.header("⚙️ Dashboard Controls")

start_date = st.sidebar.date_input(
    "Start Date",
    value=date(2024, 1, 1)
)

end_date = st.sidebar.date_input(
    "End Date",
    value=date(2024, 1, 31)
)

# ----------------------------------
# DATE VALIDATION
# ----------------------------------

if start_date > end_date:
    st.error("❌ Start Date cannot be greater than End Date.")
    st.stop()

st.write(f"Selected Period: **{start_date} → {end_date}**")

# ----------------------------------
# LAYER SELECTION
# ----------------------------------

layer_choice = st.sidebar.radio(
    "🛰️ Select Satellite Layer",
    [
        "MODIS AOD",
        "Sentinel-5P NO₂"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
🌍 Air Quality Dashboard

Data Sources:
• MODIS AOD
• Sentinel-5P NO₂

Powered by:
Google Earth Engine
"""
)

# ----------------------------------
# STATISTICS CARDS
# ----------------------------------

try:

    if layer_choice == "MODIS AOD":

        avg_aod, image_count = get_aod_stats(
            start_date,
            end_date
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🌫️ Average AOD",
                f"{avg_aod:.2f}"
            )

        with col2:
            st.metric(
                "🛰️ Images Used",
                image_count
            )

    else:

        avg_no2, image_count = get_no2_stats(
            start_date,
            end_date
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🏭 Average NO₂",
                f"{avg_no2:.6f}"
            )

        with col2:
            st.metric(
                "🛰️ Images Used",
                image_count
            )

except:
    pass

# ----------------------------------
# CREATE MAP
# ----------------------------------

m = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5,
    control_scale=True
)

# ----------------------------------
# LOAD SELECTED LAYER
# ----------------------------------

try:

    if layer_choice == "MODIS AOD":

        layer = get_aod_layer(
            start_date,
            end_date
        )

        folium.TileLayer(
            tiles=layer["tile_fetcher"].url_format,
            attr="Google Earth Engine",
            name="MODIS AOD",
            overlay=True,
            control=True
        ).add_to(m)

        st.subheader(
            "🌫️ MODIS Aerosol Optical Depth (AOD)"
        )

        st.info("""
Blue → Low Aerosol

Green → Moderate Aerosol

Yellow → High Aerosol

Red → Very High Aerosol
""")

    else:

        layer = get_no2_layer(
            start_date,
            end_date
        )

        folium.TileLayer(
            tiles=layer["tile_fetcher"].url_format,
            attr="Google Earth Engine",
            name="Sentinel-5P NO₂",
            overlay=True,
            control=True
        ).add_to(m)

        st.subheader(
            "🏭 Sentinel-5P NO₂ Concentration"
        )

        st.info("""
Blue → Low NO₂

Cyan → Moderate NO₂

Yellow → High NO₂

Red → Very High NO₂
""")

except Exception:

    st.warning(
        "⚠️ No satellite data available for the selected date range. Please choose another date range."
    )

    st.stop()

# ----------------------------------
# MAP CONTROLS
# ----------------------------------

folium.LayerControl().add_to(m)

# ----------------------------------
# DISPLAY MAP
# ----------------------------------

folium_static(
    m,
    width=1200,
    height=650
)

# ----------------------------------

# DOWNLOAD REPORTS

# ----------------------------------

try:
    if layer_choice == "MODIS AOD":

        report_df = pd.DataFrame({
            "Start Date": [start_date],
            "End Date": [end_date],
            "Layer": ["MODIS AOD"],
            "Average Value": [round(avg_aod, 2)],
            "Images Used": [image_count]
        })
    else:

        report_df = pd.DataFrame({
            "Start Date": [start_date],
            "End Date": [end_date],
            "Layer": ["Sentinel-5P NO₂"],
            "Average Value": [round(avg_no2, 6)],
            "Images Used": [image_count]
        })

    st.subheader("📥 Download Report")

    csv = report_df.to_csv(index=False)

    st.download_button(
        label="📄 Download CSV Report",
        data=csv,
        file_name="air_quality_report.csv",
        mime="text/csv"
    )

except:
    pass

try:
    if layer_choice == "MODIS AOD":

        pdf_data = generate_pdf_report(
            start_date,
            end_date,
        "   MODIS AOD",round(avg_aod, 2),
            image_count
        )
    else:
        pdf_data = generate_pdf_report(
            start_date,
            end_date,
            "Sentinel-5P NO₂",
            round(avg_no2, 6),
            image_count
        )

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_data,
        file_name="air_quality_report.pdf",
        mime="application/pdf"
    )


except:
    pass


# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.caption(
    "Air Quality & Aerosol Mapping using MODIS and Sentinel-5P | Google Earth Engine + Streamlit"
)