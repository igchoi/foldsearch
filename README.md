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

## How to run __Foldsearch__
* Clone this repository
```
git clone https://github.com/igchoi/foldsearch.git
```
* Installing target DB as indicated in [__foldseek__](https://github.com/steineggerlab/foldseek). It took ~ 5 min.
```
# after git-clone the repository, go to your cloned 'mysite' directory
cd foldsearch
cd mysite

# install alphafold db remotely
foldseek databases Alphafold/Proteome afdb tmp
```
* Now, you are ready to run __Foldsearch__. Run __django__ server & visit the server (http://127.0.0.1:8000/) with your browser (e.g. Chrome).
```
python manage.py runserver
```

* Upload __test.pdb__ using __Foldsearch__ WebApp and test the function.
