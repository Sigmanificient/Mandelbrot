# Mandelbrot [![CodeFactor](https://www.codefactor.io/repository/github/sigmanificient/mandelbrot/badge)](https://www.codefactor.io/repository/github/sigmanificient/mandelbrot)

<img src="https://github.com/sigmanificient/mandelbrot/blob/master/screenshots/1.png" alt="screenshot" height="320px" width="auto">


A pygame renderer for the mandelbrot well-known fractal.


## Requirements
```
numba~=0.53.1
pygame~=2.0.1
```

## Controls
- `f` *toggle* : flush screen for each render
- `e` *toggle* : show red progress bar
- `0-9`: *toggle* : enable/disable a filter

### Adding your filter:
You can add your very own filter at line 62, that you'll be able to use.
<br>**<!>** *It needs to be a valid Filter object*
