import streamlit as st
import subprocess

# Define the Streamlit app
def app():
    # Set the title of the app
    st.title("SRR File Information")

    # Define a text input for the SRR IDs
    srr_input = st.text_input("Enter SRR IDs (separated by commas)")

    # If the user has entered SRR IDs, display information about each SRR file
    if srr_input:
        # Split the input string into a list of SRR IDs
        srr_ids = [srr_id.strip() for srr_id in srr_input.split(",")]

        # Display information about each SRR file
        for srr_id in srr_ids:
            st.write(f"**SRR ID:** {srr_id}")

            # Use subprocess to run the SRA-tools `vdb-dump` command and capture the output
            cmd = f"vdb-dump {srr_id}"
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")

            # Display the output
            st.code(output)
            
#to be improved with subprocess.run(["prefetch", srr_id])

            # Add a download button to download the SRA file
            sra_filename = f"{srr_id}.sra"
            st.write(f"Download the SRA file: [{sra_filename}](https://www.ncbi.nlm.nih.gov/sra/?term={srr_id})")
