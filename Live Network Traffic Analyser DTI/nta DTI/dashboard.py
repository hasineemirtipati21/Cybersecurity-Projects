import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Network Traffic Analyzer", layout="centered")

st.title("Network Traffic Monitoring")

placeholder = st.empty()

packet_history = []

while True:

    data = pd.read_csv(
        "traffic_data.csv",
        names=["Source","Destination","Protocol","Size"]
    )

    with placeholder.container():

        total_packets = len(data)

        # Network status indicator
        if total_packets < 100:
            st.success("🟢 Network Status: Normal")
        elif total_packets < 300:
            st.warning("🟡 Network Status: Moderate Traffic")
        else:
            st.error("🔴 Network Status: Heavy Traffic")

        # Total packets
        st.metric("Total Packets Captured", total_packets)

        # Save packet history
        packet_history.append(total_packets)

        # Live traffic graph
        st.subheader("📈 Live Network Traffic")

        fig1, ax1 = plt.subplots(figsize=(6,3))
        ax1.plot(packet_history)
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Packets")

        st.pyplot(fig1)

        # Protocol distribution
        st.subheader("📊 Protocol Distribution")

        protocol_counts = data["Protocol"].value_counts()

        fig2, ax2 = plt.subplots(figsize=(4,4))
        protocol_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax2)

        ax2.set_ylabel("")
        st.pyplot(fig2)

        # Top IP addresses
        st.subheader("🌐 Top Source IP Addresses")

        top_sources = data["Source"].value_counts()

        st.table(top_sources.head())

        # Suspicious traffic detection
        for ip, count in top_sources.items():
            if count > 50:
                st.error(f"🚨 Suspicious Traffic Detected from {ip} ({count} packets)")

    time.sleep(5)