from fpdf import FPDF

class KundliPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Kundli Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_kundli_pdf(user_data, planetary_data, filename="kundli_report.pdf"):
    pdf = KundliPDF()
    pdf.add_page()

    # User details section
    pdf.chapter_title("User Details")
    user_details = f"Name: {user_data.get('name')}\nDOB: {user_data.get('dob')}\nTime: {user_data.get('time')}\nPlace: {user_data.get('place')}"
    pdf.chapter_body(user_details)

    # Planetary positions section
    pdf.chapter_title("Planetary Positions")
    positions_text = ""
    for planet, pos in planetary_data.items():
        positions_text += f"{planet}: {pos:.2f}°\n"
    pdf.chapter_body(positions_text)

    # Additional sections like Lagna, Nakshatra, Dasha, Remedies can be added here

    pdf.output(filename)
    return filename
