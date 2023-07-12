This is an example repo to reproduce the warning in this [SO
question](https://stackoverflow.com/questions/76668897/warning-when-referencing-numpy-scalar-types).

To reproduce, clone the repo, activate a fresh venv and install the
dependencies in requirements.txt.  The change directory to "docs/" and run
``make html``. You should now see an output similar to the following.

```
Running Sphinx v6.2.1
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output...
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
/Users/pmind/ifsm/xxx/xxx/func.py:docstring of xxx.func.func:1: WARNING: py:class reference target not found: numpy.float64
generating indices... genindex py-modindex done
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 1 warning.

The HTML pages are in build/html.
```
