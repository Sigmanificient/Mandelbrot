# Mandelbrot 

[![CodeFactor](https://www.codefactor.io/repository/github/sigmanificient/mandelbrot/badge)](https://www.codefactor.io/repository/github/sigmanificient/mandelbrot)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/Mandelbrot)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/Mandelbrot)
![Lines of code](https://img.shields.io/tokei/lines/github/Sigmanificient/Mandelbrot)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/Mandelbrot)

![](https://github.com/sigmanificient/mandelbrot/blob/master/screenshots/1.png)
A pygame renderer for the mandelbrot well-known fractal.

## Requirements
```requirements.txt
numba~=0.53.1
pygame~=2.0.1
```

## Controls
  - `f` *toggle* : flush screen for each render
  - `e` *toggle* : show red progress bar
  - `0-9`: *toggle* : enable/disable a filter

### Adding your filter
You can add your very own filter at line 62, that you'll be able to use.
<br>**<!>** *It needs to be a valid Filter object*
