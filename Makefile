.PHONY: all install model handbook clean

# Rebuild everything (model, then handbook).
all: model handbook

# One-time: install Python deps and the headless browser used to render the PDF.
install:
	pip install -r requirements.txt
	playwright install chromium

# The integrated LBO model workbook.
model:
	python3 build_model.py

# The print-ready handbook PDF (reads pe_course_notes.md + snap_*.png).
handbook:
	python3 build_handbook.py

# Remove regenerable build artifacts (keeps the .pdf and .xlsx).
clean:
	rm -f pe_course_handbook.html
	rm -rf __pycache__ pe_analytics/__pycache__ _snap
