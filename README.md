# AUTOMATED-REPORT-GENERATION

*COMPANY NAME* : CODTECH IT SOLUTIONS

*NAME*         : Hari Prasath C

*INTERN ID*    : CT04DF2838

*DOMAIN*       : PYTHON PROGRAMMING

*DURATION*     : 4 WEEKS

*MENTOR*       : NEELA SANTHOSH

*DESCRIPTION*

This project is focused on developing a Python script that reads data from a file, performs a basic analysis, and generates a well-formatted PDF report using the FPDF library. The core idea is to automate the process of reading structured data (such as student marks), analyzing it (for example, finding the average), and then creating a polished document that can be easily shared or printed.As a beginner in Python, I wanted to take up a practical task that would help me understand how real-world data is handled. Reading from a file and converting that information into a report seemed like a very useful skill to learn. So, I decided to work on a student marks report system where the marks of students are taken from a CSV file, and the system creates a neat PDF summarizing the data.The input for the script is a .csv (Comma-Separated Values) file, which contains data like the names of students, the subject they wrote, and the marks they scored. This format is very commonly used in industries and educational setups for storing structured data. It can be created easily using any spreadsheet software like Excel or even a simple text editor. In this case, I manually created a small file with four or five sample entries for testing.To read the data, I used the pandas library in Python. Pandas is extremely useful when it comes to reading and handling tabular data. With just a single line of code, I was able to read the CSV file into a DataFrame, which allowed me to access individual columns and perform calculations like averages. For example, to calculate the average marks of all students, I just used the mean() function on the “Marks” column. This step helped me learn how to extract specific information from a data table and perform calculations on it.Once the data was analyzed, I used the fpdf library to create the PDF report. FPDF is a lightweight library in Python that lets you build PDF files using simple commands. I started by adding a title to the report, followed by the table headers like "Name", "Subject", and "Marks". Then I used a loop to go through each row in the data and display each student's details in the PDF.After the table, I also included the average marks in a separate line to show a summary of the class performance. Additionally, to make the report more complete and professional, I included the current date of generation, my name as the report creator, my department and college name, and a space for a signature.The PDF file is then saved to the same folder as the script and can be opened using any PDF reader like Chrome, Edge, or Adobe Reader. One of the final touches I added was a line of code that automatically opens the PDF after it’s created, so I can immediately check the result without manually opening the file.This project taught me several important concepts: how to read and process data from files, how to do basic analysis like finding averages, and how to generate documents in a professional format. These are all practical skills that can be applied in real-life situations like creating mark sheets, attendance reports, invoices, or summaries of any dataset.More than just writing code, this task helped me understand the importance of automation in report generation. Instead of typing everything manually into Word or Excel, now I know how to create reports directly from raw data using Python. It’s a skill that I hope to expand in future projects, possibly by adding charts or using more advanced layouts in the PDF.

Overall, this was a simple but very useful project for a beginner like me to understand how programming can be used for real-world reporting tasks.

*OUTPUT OF THE TASK*

![Image](https://github.com/user-attachments/assets/0fa48789-2a06-4881-a765-24bc7fb8c132)
