setup: 
	python -m venv venv && \
	pip install -r requirements.txt && \

chat:
	python src/base.py "$(question)"
