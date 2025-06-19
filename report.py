import pandas as pd
from fpdf import FPDF
from datetime import datetime


# Read data
data = pd.read_csv("data.csv")

# Analyze data
average_marks = data["Marks"].mean()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
pdf.ln(10)

# Table headers
pdf.set_font("Arial", size=11)
pdf.cell(60, 10, "Name", 1)
pdf.cell(60, 10, "Subject", 1)
pdf.cell(30, 10, "Marks", 1)
pdf.ln()

# Table rows
for index, row in data.iterrows():
    pdf.cell(60, 10, row["Name"], 1)
    pdf.cell(60, 10, row["Subject"], 1)
    pdf.cell(30, 10, str(row["Marks"]), 1)
    pdf.ln()

# Summary (average marks)
pdf.ln(10)
pdf.cell(200, 10, f"Average Marks: {average_marks:.2f}", ln=True)

# Additional Information
current_date = datetime.now().strftime("%d-%m-%Y")
pdf.cell(200, 10, f"Date: {current_date}", ln=True)
pdf.cell(200, 10, "Institution: SJCE - Dept. of EEE", ln=True)
pdf.cell(200, 10, "Prepared by: Hari Prasath", ln=True)
pdf.cell(200, 10, "Signature: ____________________", ln=True)


# Summary (Average)
pdf.ln(10)
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)

# Save the PDF
pdf.output("marks_report.pdf")

# Save PDF
pdf.output("marks_report.pdf")
print("PDF created successfully!")


print("PDF report created successfully!")
