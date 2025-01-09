.PHONY: run
run:
	manim-slides render main.py Presentation && \
	manim-slides Presentation && \
	manim-slides convert Presentation presentation.html
