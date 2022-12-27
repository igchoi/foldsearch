# FoldSearch
* __FoldSearch__ is a WebAPP based on Django and HTML5. __FoldSearch__ is developed for searching structurally similar folds with a given input structure file (e.g. PDB).
This APP searches against in-house database or locally installed alphafold proteome DB. The searching is carried out by locally installed [foldseek](https://search.foldseek.com/search). 
## Installation
* All packages are pre-installed in _Anaconda_ virtural environment. 

```
conda create -n foldsearch
conda activate foldsearch
conda install django
conda install -c conda-forge -c bioconda foldseek
```
* Installing target DB as indicated in [__foldseek__](https://github.com/steineggerlab/foldseek). It took ~ 5 min.
```
# alphafold db
foldseek databases Alphafold/Proteome afdb tmp
```
## How to run the WebAPP
* Clone this repository & run __django__ server. You can visit the server (http://127.0.0.1:8000/) with your browser (e.g. Chrome).
```
git clone https://github.com/igchoi/foldsearch.git
cd mysite
python manage.py runserver
```
