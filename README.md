# Grammar-Correction

Steps:
1. Create virtual environment -> conda create -n grammar_correction python=3.7
2. Activate virtual environment -> conda activate grammar_correction
3. Downgrade pip -> python -m pip install pip==20.1.1
4. Install python-levenshtein -> conda install -c conda-forge python-levenshtein
5. Install Gramformer -> pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
6. Install NLTK -> pip install nltk
7. Install torch -> conda install pytorch torchvision torchaudio cpuonly -c pytorch
8. Install SymSpell -> pip install -U symspellpy
9. Download en model -> python -m spacy download en (requires Admin privileges)
10. Install Flask -> pip install Flask
11. Run application -> python grammer_correction_app.py