from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from textwrap import wrap

def create_sample_pdf():
    c = canvas.Canvas("hello.pdf", pagesize=letter)
    width, height = letter
    
    text = """Artificial Intelligence (AI) is one of the most transformative technologies of the 21st century. It has the potential to revolutionize every industry, from healthcare to finance, and even education. AI systems are capable of analyzing large amounts of data, learning patterns, and making predictions or decisions with minimal human intervention. However, despite its advantages, AI also raises ethical concerns such as privacy, bias, and job displacement. As a result, it is crucial to ensure that AI is developed and used responsibly."""
    
    # Set font and size
    c.setFont("Helvetica", 12)
    
    # Split text into wrapped lines
    y = height - 50  # Start 50 points from top
    for line in wrap(text, 80):  # Wrap at 80 characters
        c.drawString(50, y, line)
        y -= 20  # Move down 20 points
    
    c.save()

if __name__ == "__main__":
    create_sample_pdf()
