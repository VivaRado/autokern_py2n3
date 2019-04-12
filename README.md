Type Facet Autokern Python2 and Python3 without EFO

Run:

```python autokern/AutokernDemo.py```

or

```python3 autokern/AutokernDemo.py```

The test runs on Advent Pro. Keep in mind the kerning script requires decomponentized UFO. The current UFO of Advent has components, so you might the "$" sign being kerned as "|" if you pass a decomp. version it will work normally. Decomponentization is not included in this repo. You can check TYPL for that. We will reintegrate this script to VivaRado TYPL as during conversion to python3 previously, we had inflation issues.

For more information about how to use this tool visit [typefacet](https://github.com/charlesmchen/typefacet)