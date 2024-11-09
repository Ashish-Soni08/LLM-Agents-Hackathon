# Environemnt Setup

```bash
python -V
# Output: 3.12.1
```

```bash
python -m venv lab-01
```

```bash
source lab-01/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
# create a Jupyter Notebook kernel
pip install jupyter ipykernel
```

```bash
# add the virtual environment as a kernel for the jupyter notebook
python -m ipykernel install --user --name=lab-01 --display-name="Py3.12-lab-01"
```

```bash
# verify kernel installation
jupyter kernelspec list
```
