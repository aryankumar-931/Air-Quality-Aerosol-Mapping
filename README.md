# 🌍 Air Quality & Aerosol Mapping using MODIS and Sentinel-5P

## 📌 Project Overview

Air Quality & Aerosol Mapping is a Remote Sensing and GIS-based web application developed using Python, Google Earth Engine, and Streamlit.

The application visualizes satellite-derived air quality indicators over India using:

* MODIS Aerosol Optical Depth (AOD)
* Sentinel-5P Nitrogen Dioxide (NO₂)

Users can interactively explore air quality patterns, select custom date ranges, generate reports, and analyze satellite observations through an intuitive dashboard.

---

## 🚀 Features

### 🌫️ MODIS Aerosol Optical Depth (AOD)

* Visualizes aerosol concentration over India
* Dynamic date range filtering
* Interactive map visualization

### 🏭 Sentinel-5P NO₂ Monitoring

* Displays tropospheric NO₂ concentration
* Satellite-based pollution monitoring
* Layer switching support

### 📊 Dashboard Analytics

* Average AOD calculation
* Average NO₂ calculation
* Satellite image count statistics

### 📥 Reporting

* CSV Report Download
* PDF Report Download

### 🗺️ Interactive Mapping

* Folium-based map visualization
* Google Earth Engine integration
* Layer controls

### ⚠️ Smart Error Handling

* User-friendly warnings
* Invalid date range detection
* Missing data handling

---

## 🛠️ Technology Stack

* Python
* Google Earth Engine (GEE)
* Streamlit
* Folium
* Pandas
* ReportLab
* Remote Sensing
* GIS

---

## 📂 Project Structure

```text
Air-Quality-Aerosol-Mapping/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   └── air_quality_layers.py
│
├── outputs/
│
└── screenshots/
```

---

## 📷 Demo Screenshot
Here is a preview of the Air Quality & Aerosol Mapping:

![Demo Screenshot](images/demo.png)
![Demo Screenshot](images/demo1.png)
![Demo Screenshot](images/demo2.png)
![Demo Screenshot](images/demo3.png)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Air-Quality-Aerosol-Mapping
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🌎 Data Sources

### MODIS

NASA MODIS Aerosol Product

Dataset:
MCD19A2_GRANULES

### Sentinel-5P

Copernicus Atmosphere Monitoring

Dataset:
L3 NO₂

---

## 📈 Future Enhancements

* City-wise Air Quality Analysis
* AQI Classification
* Time-Series Visualization
* Historical Trend Analysis
* Multi-country Support
* Automated Report Scheduling

---

## 👨‍💻 Author

Aryan

AI Engineering Student

Remote Sensing | GIS | Machine Learning | Data Analytics

```
```
