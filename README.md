# eFlows4HPC Software Stack Documentation

Online documentation: https://eflows4hpc.readthedocs.io/

This repository provides the sources and build scripts for the on-line documentation of the eFlows4HPC Software Stack.

Follow the next steps to build the documentation pages in your current machine.

## 1. Dependencies

* python3

```
sudo zypper install python3
# or
sudo apt-get install python3
```


Some OS do not include pip3 (e.g. Ubuntu, which provides just pip).
To make sure that you are using the Python 3 pip, create an alias:

```
alias pip3=`python3 -m pip`
```

* Python 3 dependencies
```
pip3 install sphinx --user
pip3 install sphinxcontrib.contentui --user
pip3 install six --upgrade
pip3 install nbsphinx --user
pip3 install sphinx-copybutton --user
pip3 install sphinxcontrib-svg2pdfconverter --user
pip3 install rst2pdf --user
pip3 install sphinxcontrib-bibtex --user
pip3 install pandoc --user
pip3 install ipywidgets --user
pip3 install sphinx-rtd-theme==0.5.0.rc1
pip3 install prompt-toolkit --user
pip3 install ipython --user
pip3 install sphinxcontrib.yt --user
```

* System dependencies

  * For Ubuntu:

  ```
  sudo apt-get install pandoc
  sudo apt-get install librsvg2-bin
  ```
  * For OpenSuse:

    ```
    sudo zypper install pandoc
    sudo zypper install python3-Sphinx-latex
    sudo zypper install rsvg-view
    ```

* Latex packages:

  * For Ubuntu:

  ````
  sudo apt install texlive-latex-extra
  sudo apt-get install -y latexmk
  ````
  *For OpenSuse:

    ```
    sudo zypper install texlive-footnotebackref texlive-datetime texlive-epigraph texlive-eso-pic texlive-lipsum texlive-footnotebackref texlive-setspace texlive-amsmath texlive-amsfonts texlive-amstex texlive-lipsum texlive-fancyhdr texlive-anyfontsize
    ```


## 2. Build documentation

**Note**: Remember to install the dependencies before trying to build the documentation 
 from sources.

```
./build.sh
```

