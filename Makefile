clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

requirements:
	poetry export -o requirements.txt --without-hashes

requirements-dev:
	poetry export --dev -o requirements-dev.txt --without-hashes
