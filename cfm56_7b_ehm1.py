import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="CFM56-7B Engine Monitoring", layout="wide")

st.title("CFM56-7B ENGINE HEALTH MONITORING")
st.subheader("Create by Y.A. Prasetya")

# ==============================
# LIMIT CONFIGURATION
# ==============================

limits = {
    "N1":102,
    "N2":105,
    "Oil Pressure":60,
    "Oil Temp":150,
    "Fuel Flow":5200,
    "EGT":950,
    "Vibration":4
}

# ==============================
# STATUS CHECK FUNCTION
# ==============================

def check_status(value, limit):

    caution = limit * 0.95

    if value > limit:
        return "WARNING","red"

    elif value >= caution:
        return "CAUTION","orange"

    else:
        return "Normal","green"


# ==============================
# MAINTENANCE ADVICE
# ==============================

def maintenance_advice(param):

    advice = {

        "EGT":
        """Possible Cause:
• Combustion inefficiency
• Dirty fuel nozzle
• Compressor efficiency drop

Maintenance Recommendation:
• Borescope inspection
• Engine performance check""",

        "Fuel Flow":
        """Possible Cause:
• Fuel control unit degradation
• Combustion inefficiency

Maintenance Recommendation:
• Inspect fuel control unit
• Check fuel nozzle condition""",

        "Vibration":
        """Possible Cause:
• Rotor imbalance
• Bearing wear
• Fan blade damage

Maintenance Recommendation:
• Perform vibration analysis
• Inspect fan blades and bearings""",

        "Oil Pressure":
        """Possible Cause:
• Oil pump malfunction
• Oil filter blockage

Maintenance Recommendation:
• Inspect lubrication system""",

        "Oil Temp":
        """Possible Cause:
• Oil cooler inefficiency
• High engine load

Maintenance Recommendation:
• Inspect oil cooler system"""
    }

    return advice.get(param,"Engine inspection recommended")


# ==============================
# SESSION DATA STORAGE
# ==============================

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame()

# ==============================
# AIRCRAFT INFORMATION
# ==============================

st.header("Aircraft Information")

col1,col2,col3,col4 = st.columns(4)

date = col1.date_input("Date",datetime.today())
reg = col2.text_input("Aircraft Registration")
engine = col3.text_input("Engine No")
route = col4.text_input("Route")

# ==============================
# ENGINE START MONITORING
# ==============================

st.header("Engine Start Monitoring")

egt_start = st.number_input("EGT Start (°C)")

if egt_start > 725:

    st.error("WARNING : HOT START DETECTED")

    st.write("""
Possible Cause:
• Excessive fuel during start
• Ignition delay

Maintenance Recommendation:
• Combustion chamber inspection
• Check fuel nozzle
""")

# ==============================
# TAKEOFF PARAMETERS
# ==============================

st.header("Takeoff Parameter Monitoring")

col1,col2,col3 = st.columns(3)

N1 = col1.number_input("N1 (%)")
N2 = col2.number_input("N2 (%)")
EGT = col3.number_input("EGT Takeoff (°C)")

col4,col5,col6 = st.columns(3)

oil_press = col4.number_input("Oil Pressure (psi)")
oil_temp = col5.number_input("Oil Temp (°C)")
fuel_flow = col6.number_input("Fuel Flow (pph)")

vibration = st.number_input("Vibration (ips)")

# ==============================
# PARAMETER STATUS
# ==============================

st.header("Engine Status")

params = {
    "N1":N1,
    "N2":N2,
    "Oil Pressure":oil_press,
    "Oil Temp":oil_temp,
    "Fuel Flow":fuel_flow,
    "EGT":EGT,
    "Vibration":vibration
}

for p,v in params.items():

    limit = limits[p]

    status,color = check_status(v,limit)

    st.markdown(f"**{p} : {v} → :{color}[{status}]**")

    if status != "Normal":
        st.warning(maintenance_advice(p))


# ==============================
# ADD DATA TO FLEET
# ==============================

if st.button("Add Aircraft Data"):

    new_data = {

        "Date":date,
        "Aircraft":reg,
        "Engine":engine,
        "Route":route,
        "EGT Start":egt_start,
        "N1":N1,
        "N2":N2,
        "EGT":EGT,
        "Fuel Flow":fuel_flow,
        "Oil Pressure":oil_press,
        "Oil Temp":oil_temp,
        "Vibration":vibration
    }

    st.session_state.data = pd.concat(
        [st.session_state.data,pd.DataFrame([new_data])],
        ignore_index=True
    )

    st.success("Aircraft Data Added")

# ==============================
# DISPLAY FLEET DATA
# ==============================

st.header("Fleet Monitoring Data")

st.dataframe(st.session_state.data)

# ==============================
# TREND GRAPH
# ==============================

st.header("Engine Trend Monitoring")

if not st.session_state.data.empty:

    col1,col2,col3 = st.columns(3)

    # EGT TAKEOFF TREND
    with col1:

        st.subheader("EGT Takeoff Trend")

        fig1 = plt.figure(figsize=(3,2))

        plt.plot(st.session_state.data["EGT"],marker='o')

        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        st.pyplot(fig1)

    # FUEL FLOW TREND
    with col2:

        st.subheader("Fuel Flow Trend")

        fig2 = plt.figure(figsize=(3,2))

        plt.plot(st.session_state.data["Fuel Flow"],marker='o')

        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        st.pyplot(fig2)

    # VIBRATION TREND
    with col3:

        st.subheader("Vibration Trend")

        fig3 = plt.figure(figsize=(3,2))

        plt.plot(st.session_state.data["Vibration"],marker='o')

        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        st.pyplot(fig3)

# ==============================
# SAVE DATA
# ==============================

st.header("Report")

if st.button("Save Data"):

    st.session_state.data.to_csv("engine_monitoring.csv",index=False)

    st.success("Data saved successfully")

if st.button("PRINT REPORT"):

    st.info("Use browser print (CTRL + P)")